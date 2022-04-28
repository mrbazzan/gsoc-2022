import re
import sys
from itertools import chain
from argparse import Namespace, ArgumentTypeError

from transpose.cipher import Cipher
from transpose.plugincore import PluginCore
from transpose.cli import Parser


def non_negative_int(string):
    if not re.fullmatch("[1-9]+", string):
        raise ArgumentTypeError(
            f'{repr(string)} is not a positive integer'
        )
    return int(string)


class RailFencePlugin(PluginCore):
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


class RailFenceCipher(Cipher):
    def encrypt(self, msg: str, *args, **kwargs) -> str:

        # Ensure only alpha-numeric characters
        msg = [char for char in msg if char.isalnum()]
        msg_len = len(msg)

        rails = kwargs["rails"]
        rail_fence = [[] for _ in range(rails)]

        try:
            assert msg_len % (2*(rails-1)) == 0
        except AssertionError:
            print("Length of string to be must be multiple of 2(rails-1)")
            sys.exit(2)

        # [0, 1, 2, 3, 2, 1]
        _index = list(chain(range(rails-1), range(rails-1, 0, -1)))
        for i, element in enumerate(msg):
            index = _index[i % (rails+1)]
            rail_fence[index].append(element)

        text = " ".join(["".join(rail) for rail in rail_fence])
        return text

    def decrypt(self, ciphertext: str, *args, **kwargs) -> str:
        pass


plugin = RailFencePlugin()
