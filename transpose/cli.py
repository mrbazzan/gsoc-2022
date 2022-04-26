import argparse

from transpose import Singleton


class BaseParser(argparse.ArgumentParser):
    """Common options parser."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_argument(
            "text",
            type=str,
            help="Text to encrypt/decrypt"
        )

        group = self.add_mutually_exclusive_group(required=True)
        group.add_argument(
            "-c", "--encrypt",
            default=False,
            action="store_true",
            help="encrypt message"
        )

        group.add_argument(
            "-d", "--decrypt",
            default=False,
            action="store_true",
            help="decrypt message"
        )


class Parser(argparse.ArgumentParser, metaclass=Singleton):
    """
    Main CLI parser.

    Each cipher plugin that wishes to add CLI options needs to hook into this
    parser.
    """

    def __init__(self):
        super().__init__(
            conflict_handler="resolve",
            description="transposition cipher tool",
        )

        self.subparsers = self.add_subparsers(metavar="CIPHER",
                                              parser_class=BaseParser,
                                              required=True)
