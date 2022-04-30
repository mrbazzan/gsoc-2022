
import sys
from itertools import chain

from transpose.cipher import Cipher


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
