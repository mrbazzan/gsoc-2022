import sys
from typing import List
from pkg_resources import resource_filename
from importlib import import_module
from pathlib import Path

from transpose.cli import Parser
from transpose.plugincore import PluginCore


def _import_module(path):
    try:
        return import_module(f"transpose.plugins.{path.stem}")
    except ModuleNotFoundError:
        print("Can't import package %s" % path.stem)  # TODO: Find better message
        sys.exit(2)


class Application():
    def __init__(self):
        self.plugins = self.__load_plugins()

    @staticmethod
    def __load_plugins() -> List[PluginCore]:
        # IMPLEMENT ME!
        # use resource_filename(__name__, "plugins/")) to search for plugins
        plugins = []
        plugin_path = Path(resource_filename(__name__, "plugins/"))
        for path in plugin_path.iterdir():
            if path.is_file() or path.stem == "__pycache__":
                continue
            plugin = _import_module(path)
            plugins.append(plugin.Plugin())

        return plugins

    def run(self) -> None:
        args = Parser().parse_args()
        # IMPLEMENT ME!
        args.func.entry_point(args)
