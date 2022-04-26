import abc

from argparse import Namespace


class PluginCore(metaclass=abc.ABCMeta):
    def __init__(self):
        self.register()

    @abc.abstractmethod
    def register(self) -> None:
        """Register a plugin with the main CLI parser if needed."""
        pass

    @abc.abstractmethod
    def entry_point(self, args: Namespace) -> None:
        """Plugin implementation entry point."""
        pass
