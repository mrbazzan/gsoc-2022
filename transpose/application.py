from typing import List
from pkg_resources import resource_filename

from transpose.cli import Parser
from transpose.plugincore import PluginCore


class Application():
    def __init__(self):
        self.plugins = self.__load_plugins()

    @staticmethod
    def __load_plugins() -> List[PluginCore]:
        # IMPLEMENT ME!
        # use resource_filename(__name__, "plugins/")) to search for plugins
        pass

    def run(self) -> None:
        args = Parser().parse_args()
        # IMPLEMENT ME!
        pass
