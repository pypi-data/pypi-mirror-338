# Copyright (c) 2023-2024 Datalayer, Inc.
#
# Datalayer License

"""Config handler."""

import json

import tornado

from jupyter_server.base.handlers import APIHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin

from jupyter_kernels.__version__ import __version__


class ConfigHandler(ExtensionHandlerMixin, APIHandler):
    """The handler for configurations."""

    @tornado.web.authenticated
    def get(self):
        """Returns the configurations of the server extensions."""
        """
        "configuration": dict(
            [
                (
                    ''.join(
                        w.title() if idx > 0 else w
                        for idx, w in enumerate(k.split('_'))
                    ),
                    v
                ) for k, v in self.settings[f'{self.name}_config'].items()
            ]
        )
        """
        res = json.dumps({
            "extension": self.name,
            "version": __version__,
            "configuration": {
                "launcher": self.config["launcher"].to_dict(),
                "maxNotebookKernels": self.config.max_notebook_kernels,
                "maxCellKernels": self.config.max_cell_kernels,
            }
        })
        self.finish(res)
