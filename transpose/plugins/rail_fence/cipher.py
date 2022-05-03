
import sys
from itertools import chain

from transpose.cipher import Cipher


class RailFenceCipher(Cipher):

    @staticmethod
    def assert_str_length(string, rails):
        assert isinstance(string, list)
        assert isinstance(rails, int)
        try:
            assert len(string) % (2*(rails-1)) == 0
        except AssertionError:
            print("Length of string to be must be multiple of 2(rails-1)")
            sys.exit(2)

    @staticmethod
    def remove_space(msg):
        """Remove space from a string"""
        return [char for char in msg if not char.isspace()]

    def encrypt(self, msg: str, *args, **kwargs) -> str:
        """Encrypt plaintext to ciphertext using rails"""

        # Ensure to skip all space
        msg = self.remove_space(msg)
        rails = kwargs.get("rails")

        rail_fence = [[] for _ in range(rails)]

        self.assert_str_length(msg, rails)

        # This is the order we want to pick characters.
        _index = list(chain(range(rails-1), range(rails-1, 0, -1)))
        for i, element in enumerate(msg):
            # This is done in order to get the right index depending on the rails.
            # If rails is 2, `_index` is 2[0, 1]
            # If rails is 4, `_index` is 6[0, 1, 2, 3, 2, 1]
            # The formula, 2*(rails-1), is used to get the length of `_index`
            index = _index[i % (2*(rails-1))]
            rail_fence[index].append(element)

        text = " ".join(["".join(rail) for rail in rail_fence])
        return text

    def decrypt(self, ciphertext: str, *args, **kwargs) -> str:
        """Decrypt ciphertext to plaintext using rails"""
        text = [list(t) for t in ciphertext.split()]

        ciphertext = self.remove_space(ciphertext)
        rails = kwargs.get("rails")

        self.assert_str_length(ciphertext, rails)

        plaintext = ""

        _index = list(chain(range(rails-1), range(rails-1, 0, -1)))
        for i in range(len(ciphertext)):
            index = _index[i % (2 * (rails - 1))]
            plaintext += text[index].pop(0)

        return plaintext
