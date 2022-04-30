
import sys
from argparse import Namespace

from transpose.plugincore import PluginCore
from transpose.cli import Parser

from .cipher import RailFenceCipher
from .utils import non_negative_int


class Plugin(PluginCore):
    def register(self) -> None:
        railfenceparser = Parser().subparsers.add_parser(
            "rail_fence",
            help="Rail fence cipher"
        )
        railfenceparser.add_argument(
            "--rails",
            help="Imaginary fence used for encrypting/decrypting.",
            type=non_negative_int,
            required=True
        )
        railfenceparser.set_defaults(func=self)

    def entry_point(self, args: Namespace) -> None:
        if args.encrypt:
            print("\nCIPHERTEXT: ",
                  RailFenceCipher().encrypt(msg=args.text, rails=args.rails))
        else:
            print("\nPLAINTEXT: ",
                  RailFenceCipher().decrypt(ciphertext=args.text, rails=args.rails))
        sys.exit()
