
import sys
from argparse import Namespace

from transpose.plugincore import PluginCore
from transpose.cli import Parser
from .cipher import Vigenere


class Plugin(PluginCore):
    """Core Vigenere plugin functionality"""

    def register(self) -> None:
        """Add vigenere command to CLI interface"""
        vigenere_parser = Parser().subparsers.add_parser(
            "vigenere",
            help="Vigenere cipher"
        )
        vigenere_parser.add_argument(
            "--key",
            required=True,
            help="Keyword used for encrypting/decrypting."
        )
        vigenere_parser.set_defaults(func=self)

    def entry_point(self, args: Namespace) -> None:
        if args.encrypt:
            print("\nCIPHERTEXT: ", Vigenere().encrypt(msg=args.text, key=args.key))
        else:
            print("\nPLAINTEXT: ", Vigenere().decrypt(ciphertext=args.text, key=args.key))
        sys.exit(0)
