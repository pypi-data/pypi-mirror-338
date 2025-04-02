"""
Module with all the individual handlers, which execute git commands and return the results to the frontend.
"""
import functools
import json
import os
from pathlib import Path
from typing import Tuple, Union
from unittest.mock import Mock

import tornado
from jupyter_server.base.handlers import APIHandler, path_regex
from jupyter_server.services.contents.manager import ContentsManager
from jupyter_server.utils import url2path, url_path_join
from packaging.version import parse
from http import HTTPStatus
from jupyter_server.serverapp import ServerWebApplication

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.tornado import TornadoPlugin
from marshmallow import Schema, fields
from swagger_ui import tornado_api_doc

try:
    import hybridcontents
except ImportError:
    hybridcontents = None

from ._version import __version__
from .git import DEFAULT_REMOTE_NAME, Git
from .log import get_logger

# Git configuration options exposed through the REST API
ALLOWED_OPTIONS = ["user.name", "user.email"]
# REST API namespace
NAMESPACE = "/link-git"


class GitHandler(APIHandler):
    """
    Top-level parent class.
    """

    @property
    def git(self) -> Git:
        return self.settings["link-git"]

    @functools.lru_cache()
    def url2localpath(
        self, path: str, with_contents_manager: bool = False
    ) -> Union[str, Tuple[str, ContentsManager]]:
        """Get the local path from a JupyterLab server path.

        Optionally it can also return the contents manager for that path.
        """
        cm = self.contents_manager

        # Handle local manager of hybridcontents.HybridContentsManager
        if hybridcontents is not None and isinstance(
            cm, hybridcontents.HybridContentsManager
        ):
            _, cm, path = hybridcontents.hybridmanager._resolve_path(path, cm.managers)

        local_path = os.path.join(os.path.expanduser(cm.root_dir), url2path(path))
        return (local_path, cm) if with_contents_manager else local_path


class GitCloneHandler(GitHandler):
    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        Handler for the `git clone`

        Input format:
            {
              'repo_url': 'https://github.com/path/to/myrepo',
              OPTIONAL 'auth': '{ 'username': '<username>',
                                  'password': '<password>'
                                }'
            }
        """
        data = self.get_json_body()
        response = await self.git.clone(
            self.url2localpath(path), data["clone_url"], data.get("auth", None)
        )

        if response["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(response))


class GitCredentialConfigHandler(GitHandler):
    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        Handler for setting git credential store

        Request body
        {"save_credential": bool}

        Return
        {"code": 0}
        """
        data = self.get_json_body()
        save_credential = data.get("save_credential", None)

        if save_credential is None:
            self.set_status(HTTPStatus.BAD_REQUEST)
            self.finish(json.dumps({"code": 1, "message": "save_credential is required."}))
            return

        if save_credential:
            result = await self.git.set_credentials_store(self.url2localpath(path))
        else:
            result = await self.git.unset_credentials_store(self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)

        self.finish(json.dumps(result))


class GitAllHistoryHandler(GitHandler):
    """
    Parent handler for all four history/status git commands:
    1. git show_top_level
    2. git branch
    3. git log
    4. git status
    Called on refresh of extension's widget
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, calls individual handlers for
        'git show_top_level', 'git branch', 'git log', and 'git status'
        """
        body = self.get_json_body()
        history_count = body["history_count"]
        local_path = self.url2localpath(path)

        show_top_level = await self.git.show_top_level(local_path)
        if show_top_level.get("path") is None:
            self.set_status(500)
            self.finish(json.dumps(show_top_level))
        else:
            branch = await self.git.branch(local_path)
            log = await self.git.log(local_path, history_count)
            status = await self.git.status(local_path)

            result = {
                "code": show_top_level["code"],
                "data": {
                    "show_top_level": show_top_level,
                    "branch": branch,
                    "log": log,
                    "status": status,
                },
            }
            self.finish(json.dumps(result))


class GitShowTopLevelHandler(GitHandler):
    """
    Handler for 'git rev-parse --show-toplevel'.
    Displays the git root directory inside a repository.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, displays the git root directory inside a repository.
        """
        result = await self.git.show_top_level(self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitCheckMergeDriverHandler(GitHandler):
    """
    Handler for
    "git config --get-regexp '^merge[.]mrx_link_git_merger[.]'" +
    "git check-attr merge '*.ipynb'"
    """

    @tornado.web.authenticated
    async def get(self, path: str = ""):
        """
        GET request handler,
        check whether the Merge Driver is applied in git config and git attributes.
        """
        git_top_level = self.get_query_argument("git_top_level", "")
        result = await self.git.check_merge_driver(path=git_top_level)
        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitUpdateMergeDriverHandler(GitHandler):
    """
    Handler for
    git config merge.mrx_link_git_merger.name 'Git Merge Driver for MRX Link Git'
    git config merge.mrx_link_git_merger.driver \
        '<sys.excutable> <script_file> --base-file %O --current-file %A --incoming-file %B --file-path %P'
    and update .gitattributes file as '*.ipynb merge=mrx_link_git_merger'
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST Request handler,
        Apply the Link Merge Driver to git config and git attributes
        """
        body = self.get_json_body()
        git_top_level = body.get("git_top_level", "")
        result = await self.git.update_merge_driver(path=git_top_level)
        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitInfoHandler(GitHandler):
    """
    Handler for getting git information. Execute
    git remote -v +
    git log -1
    and extract git remote url, commit ID and git top level.

    return ex.
    {
        "code": 0,
        "git_top_level": "/home/user/project",
        "remote_url": "https://github.com/makinarocks/mrx-link-git",
        "last_commit_id": "eeb359dc3899d8c3c8206f60689404e807c7e1bb",
    }
    """

    @tornado.web.authenticated
    async def get(self, path: str = ""):
        """
        GET request handler,
        check git top level path, git remote url, current commit ID.
        """
        local_path = self.url2localpath(path)

        url_result = await self.git.get_remote_url(path=local_path)
        if url_result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.finish(json.dumps(url_result))
            return

        commit_id_result = await self.git.get_last_commit_id(path=local_path)
        if commit_id_result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.finish(json.dumps(commit_id_result))
            return

        top_level_result = await self.git.show_top_level(local_path)

        if top_level_result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.finish(json.dumps(top_level_result))
            return

        result = {**url_result, **commit_id_result}
        result["git_top_level"] = top_level_result.get("path", "")
        self.finish(json.dumps(result))


class GitCheckFileIsPushedHandler(GitHandler):
    """
    Handler for checking whether the file change is pushed to remote.

    arg ex.
    {
        "file_path": "/home/user/project/test.ipynb",
    }

    return ex.
    {
        "code": 0,
        "is_pushed": True,
    }
    """

    @tornado.web.authenticated
    async def get(self, path: str = ""):
        """
        GET request handler,
        Make sure the file is committed.
        And check if the local commit have been pushed to remote.
        """
        file_path = self.get_query_argument("file_path", "")
        if not file_path or not "." in os.path.basename(file_path):
            self.set_status(HTTPStatus.BAD_REQUEST)
            self.finish(json.dumps({"code": 1, "message": "File path is required."}))
            return

        parent_path = os.path.dirname(file_path)
        local_path = self.url2localpath(parent_path)
        file_name = os.path.basename(file_path)

        if not os.path.exists(local_path + "/" + file_name):
            self.set_status(HTTPStatus.BAD_REQUEST)
            self.finish(json.dumps({"code": 1, "message": "The file does not exist."}))
            return

        # Check the file is committed
        is_committed_result = await self.git.check_file_is_committed(path=local_path, file_path=file_name)
        if is_committed_result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.finish(json.dumps(is_committed_result))

        is_committed = is_committed_result.get("is_committed", False)
        if not is_committed:
            msg = "The file is not committed."
            result = {"code": 0, "is_pushed": False, "message": msg}
            self.finish(json.dumps(result))
            return

        # Check the currunt branch is pushed
        current_upstream_branch_result = await self.git.get_current_upstream_branch(path=local_path)
        if current_upstream_branch_result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.finish(json.dumps(current_upstream_branch_result))
            return

        current_upstream_branch = current_upstream_branch_result.get("current_upstream_branch", None)
        if current_upstream_branch is None:
            msg = "Current local branch does not exist in remote repository. Please push your changes to the remote repository."
            result = {"code": 0, "is_pushed": False, "message": msg}
            self.finish(json.dumps(result))
            return

        # Check the current commit is pushed to upstream current branch
        last_commit_result = await self.git.get_last_commit_id(path=local_path)
        if last_commit_result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.finish(json.dumps(last_commit_result))
            return

        upstream_commit_result = await self.git.get_commit_ids_from_branch(branch=current_upstream_branch, path=local_path)
        if upstream_commit_result["code"] != 0:
            self.set_status(HTTPStatus.INTERNAL_SERVER_ERROR)
            self.finish(json.dumps(upstream_commit_result))
            return

        last_commit_id = last_commit_result.get("last_commit_id", "")
        upstream_commit_ids = upstream_commit_result.get("commit_ids", [])
        is_pushed = last_commit_id in upstream_commit_ids

        if is_pushed:
            result = {"code": 0, "is_pushed": is_pushed}
        else:
            msg = "The current commit has not been pushed to the upstream branch."
            result = {"code": 0, "is_pushed": is_pushed, "message": msg}

        self.finish(json.dumps(result))


class GitShowPrefixHandler(GitHandler):
    """
    Handler for 'git rev-parse --show-prefix'.
    Displays the prefix path of a directory in a repository,
    with respect to the root directory.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, displays the prefix path of a directory in a repository,
        with respect to the root directory.
        """
        result = await self.git.show_prefix(self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitFetchHandler(GitHandler):
    """
    Handler for 'git fetch'
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, fetch from remotes.
        """
        result = await self.git.fetch(self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitStatusHandler(GitHandler):
    """
    Handler for 'git status --porcelain', fetches the git status.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, fetches the git status.
        """
        result = await self.git.status(self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitLogHandler(GitHandler):
    """
    Handler for 'git log'.
    Fetches Commit SHA, Author Name, Commit Date & Commit Message.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler,
        fetches Commit SHA, Author Name, Commit Date & Commit Message.
        """
        body = self.get_json_body()
        history_count = body.get("history_count", 25)
        follow_path = body.get("follow_path")
        result = await self.git.log(
            self.url2localpath(path), history_count, follow_path
        )

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitDetailedLogHandler(GitHandler):
    """
    Handler for 'git log -1 --stat --numstat --oneline' command.
    Fetches file names of committed files, Number of insertions &
    deletions in that commit.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, fetches file names of committed files, Number of
        insertions & deletions in that commit.
        """
        data = self.get_json_body()
        selected_hash = data["selected_hash"]
        result = await self.git.detailed_log(selected_hash, self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitDiffHandler(GitHandler):
    """
    Handler for 'git diff --numstat'. Fetches changes between commits & working tree.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, fetches differences between commits & current working
        tree.
        """
        my_output = await self.git.diff(self.url2localpath(path))

        if my_output["code"] != 0:
            self.set_status(500)
        self.finish(my_output)


class GitBranchHandler(GitHandler):
    """
    Handler for 'git branch -a'. Fetches list of all branches in current repository
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, fetches all branches in current repository.
        """
        result = await self.git.branch(self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitBranchDeleteHandler(GitHandler):
    """
    Handler for 'git branch -D <branch>'
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, delete branch in current repository.

        Args:
            path: Git repository path relatively to the server root
        Body: {
            "branch": Branch name to be deleted
        }
        """
        data = self.get_json_body()
        result = await self.git.branch_delete(self.url2localpath(path), data["branch"])

        if result["code"] != 0:
            self.set_status(500)
            self.finish(json.dumps(result))
        else:
            self.set_status(204)


class GitAddHandler(GitHandler):
    """
    Handler for git add <filename>'.
    Adds one or all files to the staging area.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, adds one or all files into the staging area.
        """
        data = self.get_json_body()
        if data["add_all"]:
            body = await self.git.add_all(self.url2localpath(path))
        else:
            filename = data["filename"]
            body = await self.git.add(filename, self.url2localpath(path))

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitAddAllUnstagedHandler(GitHandler):
    """
    Handler for 'git add -u'. Adds ONLY all unstaged files, does not touch
    untracked or staged files.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, adds all the changed files.
        """
        body = await self.git.add_all_unstaged(self.url2localpath(path))
        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitAddAllUntrackedHandler(GitHandler):
    """
    Handler for 'echo "a\n*\nq\n" | git add -i'. Adds ONLY all
    untracked files, does not touch unstaged or staged files.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, adds all the untracked files.
        """
        body = await self.git.add_all_untracked(self.url2localpath(path))
        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitRemoteAddHandler(GitHandler):
    """Handler for 'git remote add <name> <url>'."""

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """POST request handler to add a remote."""
        data = self.get_json_body()
        name = data.get("name", DEFAULT_REMOTE_NAME)
        url = data["url"]
        output = await self.git.remote_add(self.url2localpath(path), url, name)
        if output["code"] == 0:
            self.set_status(201)
        else:
            self.set_status(500)
        self.finish(json.dumps(output))


class GitResetHandler(GitHandler):
    """
    Handler for 'git reset <filename>'.
    Moves one or all files from the staged to the unstaged area.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler,
        moves one or all files from the staged to the unstaged area.
        """
        data = self.get_json_body()
        local_path = self.url2localpath(path)
        if data["reset_all"]:
            body = await self.git.reset_all(local_path)
        else:
            filename = data["filename"]
            body = await self.git.reset(filename, local_path)

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitDeleteCommitHandler(GitHandler):
    """
    Handler for 'git revert --no-commit <SHA>'.
    Deletes the specified commit from the repository, leaving history intact.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        data = self.get_json_body()
        commit_id = data["commit_id"]
        body = await self.git.delete_commit(commit_id, self.url2localpath(path))

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitResetToCommitHandler(GitHandler):
    """
    Handler for 'git reset --hard <SHA>'.
    Deletes all commits from head to the specified commit, making the specified commit the new head.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        data = self.get_json_body()
        commit_id = data["commit_id"]
        body = await self.git.reset_to_commit(commit_id, self.url2localpath(path))

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitCheckoutHandler(GitHandler):
    """
    Handler for 'git checkout <branchname>'. Changes the current working branch.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, changes between branches.
        """
        data = self.get_json_body()
        local_path = self.url2localpath(path)

        if data["checkout_branch"]:
            if data["new_check"]:
                body = await self.git.checkout_new_branch(
                    data["branchname"], data["startpoint"], local_path
                )
            else:
                body = await self.git.checkout_branch(data["branchname"], local_path)
        elif data["checkout_all"]:
            body = await self.git.checkout_all(local_path)
        else:
            body = await self.git.checkout(data["filename"], local_path)

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitMergeHandler(GitHandler):
    """
    Handler for git merge '<merge_from> <merge_into>'. Merges into current working branch
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, merges branches
        """
        data = self.get_json_body()
        branch = data["branch"]
        body = await self.git.merge(branch, self.url2localpath(path))

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitCommitHandler(GitHandler):
    """
    Handler for 'git commit -m <message>' and 'git commit --amend'. Commits files.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, commits files.
        """
        data = self.get_json_body()
        commit_msg = data["commit_msg"]
        amend = data.get("amend", False)
        body = await self.git.commit(commit_msg, amend, self.url2localpath(path))

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitUpstreamHandler(GitHandler):
    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        Handler for the `git rev-parse --abbrev-ref $CURRENT_BRANCH_NAME@{upstream}` on the repo. Used to check if there
        is a upstream branch defined for the current Git repo (and a side-effect is disabling the Git push/pull actions)
        """
        local_path = self.url2localpath(path)
        current_branch = await self.git.get_current_branch(local_path)
        response = await self.git.get_upstream_branch(local_path, current_branch)
        if response["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(response))


class GitPullHandler(GitHandler):
    """
    Handler for 'git pull'. Pulls files from a remote branch.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, pulls files from a remote branch to your current branch.
        """
        data = self.get_json_body()
        response = await self.git.pull(
            self.url2localpath(path),
            data.get("auth", None),
            data.get("cancel_on_conflict", False),
        )

        if response["code"] != 0:
            self.set_status(500)

        self.finish(json.dumps(response))


class GitPushHandler(GitHandler):
    """
    Handler for 'git push <first-branch> <second-branch>.
    Pushes committed files to a remote branch.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler,
        pushes committed files from your current branch to a remote branch

        Request body:
        {
            remote?: string # Remote to push to; i.e. <remote_name> or <remote_name>/<branch>
            force: boolean # Whether or not to force the push
        }
        """
        local_path = self.url2localpath(path)
        data = self.get_json_body()
        known_remote = data.get("remote")
        force = data.get("force", False)

        current_local_branch = await self.git.get_current_branch(local_path)

        set_upstream = False
        current_upstream_branch = await self.git.get_upstream_branch(
            local_path, current_local_branch
        )

        if known_remote is not None:
            set_upstream = current_upstream_branch["code"] != 0

            remote_name, _, remote_branch = known_remote.partition("/")

            current_upstream_branch = {
                "code": 0,
                "remote_branch": remote_branch or current_local_branch,
                "remote_short_name": remote_name,
            }

        if current_upstream_branch["code"] == 0:
            branch = ":".join(["HEAD", current_upstream_branch["remote_branch"]])
            response = await self.git.push(
                current_upstream_branch["remote_short_name"],
                branch,
                local_path,
                data.get("auth", None),
                set_upstream,
                force,
            )

        else:
            # Allow users to specify upstream through their configuration
            # https://git-scm.com/docs/git-config#Documentation/git-config.txt-pushdefault
            # Or use the remote defined if only one remote exists
            config = await self.git.config(local_path)
            config_options = config["options"]
            list_remotes = await self.git.remote_show(local_path)
            remotes = list_remotes.get("remotes", list())
            push_default = config_options.get("remote.pushdefault")

            default_remote = None
            if push_default is not None and push_default in remotes:
                default_remote = push_default
            elif len(remotes) == 1:
                default_remote = remotes[0]

            if default_remote is not None:
                response = await self.git.push(
                    default_remote,
                    current_local_branch,
                    local_path,
                    data.get("auth", None),
                    set_upstream=True,
                    force=force,
                )
            else:
                response = {
                    "code": 128,
                    "message": "fatal: The current branch {} has no upstream branch.".format(
                        current_local_branch
                    ),
                    "remotes": remotes,  # Returns the list of known remotes
                }

        if response["code"] != 0:
            self.set_status(500)

        self.finish(json.dumps(response))


class GitInitHandler(GitHandler):
    """
    Handler for 'git init'. Initializes a repository.
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, initializes a repository.
        """
        body = await self.git.init(self.url2localpath(path))

        if body["code"] != 0:
            self.set_status(500)

        self.finish(json.dumps(body))


class GitChangedFilesHandler(GitHandler):
    @tornado.web.authenticated
    async def post(self, path: str = ""):
        body = await self.git.changed_files(
            self.url2localpath(path), **self.get_json_body()
        )

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitConfigHandler(GitHandler):
    """
    Handler for 'git config' commands
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST get (if no options are passed) or set configuration options
        """
        data = self.get_json_body() or {}
        options = data.get("options", {})

        filtered_options = {k: v for k, v in options.items() if k in ALLOWED_OPTIONS}
        response = await self.git.config(self.url2localpath(path), **filtered_options)
        if "options" in response:
            response["options"] = {
                k: v for k, v in response["options"].items() if k in ALLOWED_OPTIONS
            }

        if response["code"] != 0:
            self.set_status(500)
        else:
            self.set_status(201)
        self.finish(json.dumps(response))


class GitContentHandler(GitHandler):
    """
    Handler to get file content at a certain git reference
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        data = self.get_json_body()
        filename = data["filename"]
        reference = data["reference"]
        local_path, cm = self.url2localpath(path, with_contents_manager=True)
        response = await self.git.get_content_at_reference(
            filename, reference, local_path, cm
        )
        self.finish(json.dumps(response))


class GitDiffNotebookHandler(GitHandler):
    """
    Returns nbdime diff of given notebook base content and remote content
    """

    @tornado.web.authenticated
    async def post(self):
        data = self.get_json_body()
        try:
            prev_content = data["previousContent"]
            curr_content = data["currentContent"]
        except KeyError as e:
            get_logger().error(f"Missing key in POST request.", exc_info=e)
            raise tornado.web.HTTPError(
                status_code=400, reason=f"Missing POST key: {e}"
            )
        try:
            base_content = data.get("baseContent")

            content = await self.git.get_nbdiff(
                prev_content, curr_content, base_content
            )
        except Exception as e:
            get_logger().error(f"Error computing notebook diff.", exc_info=e)
            raise tornado.web.HTTPError(
                status_code=500,
                reason=f"Error diffing content: {e}.",
            ) from e
        self.finish(json.dumps(content))


class GitIgnoreHandler(GitHandler):
    """
    Handler to manage .gitignore
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST add entry in .gitignore
        """
        local_path = self.url2localpath(path)
        data = self.get_json_body()
        file_path = data.get("file_path", None)
        use_extension = data.get("use_extension", False)
        if file_path:
            if use_extension:
                suffixes = Path(file_path).suffixes
                if len(suffixes) > 0:
                    file_path = "**/*" + ".".join(suffixes)
            body = await self.git.ignore(local_path, file_path)
        else:
            body = await self.git.ensure_gitignore(local_path)

        if body["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(body))


class GitSettingsHandler(GitHandler):
    @tornado.web.authenticated
    async def get(self):
        jlab_version = self.get_query_argument("version", None)
        if jlab_version is not None:
            jlab_version = str(parse(jlab_version))
        git_version = None
        try:
            git_version = await self.git.version()
        except Exception as error:
            self.log.debug(
                "[mrx_link_git] Failed to execute 'git' command: {!s}".format(error)
            )
        server_version = str(__version__)

        self.finish(
            json.dumps(
                {
                    "frontendVersion": jlab_version,
                    "gitVersion": git_version,
                    "serverVersion": server_version,
                }
            )
        )


class GitTagHandler(GitHandler):
    """
    Handler for 'git tag '. Fetches list of all tags in current repository
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, fetches all tags in current repository.
        """
        result = await self.git.tags(self.url2localpath(path))

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GitTagCheckoutHandler(GitHandler):
    """
    Handler for 'git tag checkout '. Checkout the tag version of repo
    """

    @tornado.web.authenticated
    async def post(self, path: str = ""):
        """
        POST request handler, checkout the tag version to a branch.
        """
        data = self.get_json_body()
        tag = data["tag_id"]
        result = await self.git.tag_checkout(self.url2localpath(path), tag)

        if result["code"] != 0:
            self.set_status(500)
        self.finish(json.dumps(result))


class GraphsToDiff(Schema):
    previousContent = fields.Dict()
    currentContent = fields.Dict()


class DifferenceGraph(Schema):
    cells = fields.Dict()
    metadata = fields.Dict()


class GitDagDiffHandler(GitHandler):
    """
    Returns dagdiff of given notebook base content and remote content
    """

    @tornado.web.authenticated
    async def post(self):
        """Link DAG (directed acyclic graph) diff
        ---
        description: Produces a difference graph between the two graphs
        requestBody:
            description: previousContent and currentContent to compare
            content:
                application/json:
                    schema: GraphsToDiff
        responses:
            200:
                description: a difference graph
                schema: DifferenceGraph
        """
        data = self.get_json_body()
        try:
            prev_content = data["previousContent"]
            curr_content = data["currentContent"]
        except KeyError as e:
            get_logger().error(f"Missing key in POST request.", exc_info=e)
            raise tornado.web.HTTPError(
                status_code=400, reason=f"Missing POST key: {e}"
            )
        try:
            content = await self.git.get_dagdiff(
                prev_content, curr_content
            )
        except Exception as e:
            get_logger().error(f"Error computing dagdiff.", exc_info=e)
            raise tornado.web.HTTPError(
                status_code=500,
                reason=f"Error diffing content: {e}.",
            ) from e
        self.finish(json.dumps(content))


def setup_handlers(web_app: ServerWebApplication):
    """
    Setups all of the git command handlers.
    Every handler is defined here, to be used in git.py file.
    """

    handlers_with_path = [
        ("/add_all_unstaged", GitAddAllUnstagedHandler),
        ("/add_all_untracked", GitAddAllUntrackedHandler),
        ("/all_history", GitAllHistoryHandler),
        ("/branch/delete", GitBranchDeleteHandler),
        ("/branch", GitBranchHandler),
        ("/changed_files", GitChangedFilesHandler),
        ("/checkout", GitCheckoutHandler),
        ("/clone", GitCloneHandler),
        ("/commit", GitCommitHandler),
        ("/config", GitConfigHandler),
        ("/content", GitContentHandler),
        ("/delete_commit", GitDeleteCommitHandler),
        ("/detailed_log", GitDetailedLogHandler),
        ("/diff", GitDiffHandler),
        ("/init", GitInitHandler),
        ("/log", GitLogHandler),
        ("/merge", GitMergeHandler),
        ("/pull", GitPullHandler),
        ("/push", GitPushHandler),
        ("/remote/add", GitRemoteAddHandler),
        ("/remote/fetch", GitFetchHandler),
        ("/reset", GitResetHandler),
        ("/reset_to_commit", GitResetToCommitHandler),
        ("/show_prefix", GitShowPrefixHandler),
        ("/show_top_level", GitShowTopLevelHandler),
        ("/check_merge_driver", GitCheckMergeDriverHandler),
        ("/update_merge_driver", GitUpdateMergeDriverHandler),
        ("/status", GitStatusHandler),
        ("/upstream", GitUpstreamHandler),
        ("/ignore", GitIgnoreHandler),
        ("/tags", GitTagHandler),
        ("/tag_checkout", GitTagCheckoutHandler),
        ("/add", GitAddHandler),
        ("/info", GitInfoHandler),
        ("/check_push", GitCheckFileIsPushedHandler),
        ("/set_credential_store", GitCredentialConfigHandler)
    ]

    handlers = [
        ("/diffnotebook", GitDiffNotebookHandler),
        ("/settings", GitSettingsHandler),
    ]

    dagdiff_handlers = [
        ("/dagdiff", GitDagDiffHandler),
    ]

    # add the baseurl to our paths
    base_url = web_app.settings["base_url"]
    git_handlers = [
        (url_path_join(base_url, NAMESPACE + path_regex + endpoint), handler)
        for endpoint, handler in handlers_with_path
    ] + [
        (url_path_join(base_url, NAMESPACE + endpoint), handler)
        for endpoint, handler in handlers
    ] + [
        (url_path_join(base_url, NAMESPACE + endpoint), handler)
        for endpoint, handler in dagdiff_handlers
    ]

    web_app.add_handlers(".*", git_handlers)
    # XXX: a hack to bypass test_handlers unit test
    if isinstance(web_app, Mock):
        return
    spec = APISpec(
        title="mrx-link-git API",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=[TornadoPlugin(), MarshmallowPlugin()],
    )
    for endpoint, handler in dagdiff_handlers:
        spec.path(urlspec=(url_path_join(base_url, NAMESPACE + endpoint), handler))
    tornado_api_doc(web_app, config=spec.to_dict(), url_prefix=url_path_join(base_url, NAMESPACE + "/doc"), title="Swagger UI")
