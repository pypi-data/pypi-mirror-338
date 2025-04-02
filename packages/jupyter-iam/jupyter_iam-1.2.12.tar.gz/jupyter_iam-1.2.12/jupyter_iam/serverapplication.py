# Copyright (c) 2023-2024 Datalayer, Inc.
#
# Datalayer License

"""The Jupyter IAM Server application."""

import os

from traitlets import default, CInt, Instance, Unicode
from traitlets.config import Configurable

from jupyter_server.utils import url_path_join
from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin

from jupyter_iam.__version__ import __version__

from jupyter_iam.handlers.index.handler import IndexHandler
from jupyter_iam.handlers.config.handler import ConfigHandler
from jupyter_iam.handlers.oauth.handler import OAuth2Callback


DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "./static")

DEFAULT_TEMPLATE_FILES_PATH = os.path.join(os.path.dirname(__file__), "./templates")


class JupyterIAMExtensionApp(ExtensionAppJinjaMixin, ExtensionApp):
    """The Jupyter IAM Server extension."""

    name = "jupyter_iam"

    extension_url = "/jupyter_iam"

    load_other_extensions = True

    static_paths = [DEFAULT_STATIC_FILES_PATH]

    template_paths = [DEFAULT_TEMPLATE_FILES_PATH]

    class Launcher(Configurable):
        """Jupyter IAM launcher configuration"""

        def to_dict(self):
            return {
                "category": self.category,
                "name": self.name,
                "icon_svg_url": self.icon_svg_url,
                "rank": self.rank,
            }

        category = Unicode(
            "",
            config=True,
            help=("Application launcher card category."),
        )

        name = Unicode(
            "Jupyter IAM",
            config=True,
            help=("Application launcher card name."),
        )

        icon_svg_url = Unicode(
            None,
            allow_none=True,
            config=True,
            help=("Application launcher card icon."),
        )

        rank = CInt(
            0,
            config=True,
            help=("Application launcher card rank."),
        )

    launcher = Instance(Launcher)

    @default("launcher")
    def _default_launcher(self):
        return JupyterIAMExtensionApp.Launcher(parent=self, config=self.config)


    def initialize_settings(self):
        self.log.debug("Jupyter IAM Config {}".format(self.config))


    def initialize_templates(self):
        self.serverapp.jinja_template_vars.update({"jupyter_iam_version" : __version__})


    def initialize_handlers(self):
        self.log.debug("Jupyter IAM Config {}".format(self.settings['jupyter_iam_jinja2_env']))
        handlers = [
            ("jupyter_iam", IndexHandler),
            (url_path_join("jupyter_iam", "config"), ConfigHandler),
            (url_path_join("jupyter_iam", "oauth2", "callback"), OAuth2Callback),
        ]
        self.handlers.extend(handlers)


# -----------------------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------------------

main = launch_new_instance = JupyterIAMExtensionApp.launch_instance
