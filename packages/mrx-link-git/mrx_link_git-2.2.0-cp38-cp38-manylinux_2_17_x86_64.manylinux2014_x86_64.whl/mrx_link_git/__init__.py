"""Initialize the backend server extension
"""

import json
from pathlib import Path
from jupyter_server.serverapp import ServerApp
from traitlets import List, Dict, Unicode
from traitlets.config import Configurable

from ._version import __version__
from .handlers import setup_handlers
from .git import Git

HERE = Path(__file__).parent.resolve()

with (HERE / "labextension" / "package.json").open(encoding="utf-8") as fid:
    data = json.load(fid)


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": data["name"]}]


class JupyterLabGit(Configurable):
    """
    Config options for mrx_link_git

    Modeled after: https://github.com/jupyter/jupyter_server/blob/9dd2a9a114c045cfd8fd8748400c6a697041f7fa/jupyter_server/serverapp.py#L1040
    """

    actions = Dict(
        help="Actions to be taken after a git command. Each action takes a list of commands to execute (strings). Supported actions: post_init",
        config=True,
        trait=List(
            trait=Unicode(), help='List of commands to run. E.g. ["touch baz.py"]'
        )
        # TODO Validate
    )


def _jupyter_server_extension_points():
    return [{"module": "mrx_link_git"}]


def _load_jupyter_server_extension(server_app: ServerApp):
    """Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    server_app: jupyter_server.serverapp.ServerApp
        JupyterLab application instance
    """
    if not server_app.contents_manager.allow_hidden:
        server_app.contents_manager.allow_hidden = True

    config = JupyterLabGit(config=server_app.config)
    server_app.web_app.settings["link-git"] = Git(config)
    setup_handlers(server_app.web_app)


# For backward compatibility
load_jupyter_server_extension = _load_jupyter_server_extension
