
from transpose.cipher import Cipher


class Vigenere(Cipher):
    """Vigenere Cipher class"""

    @staticmethod
    def _implement(msg, sign, *args, **kwargs):
        # All printable ASCII characters
        total = [chr(i) for i in range(32, 127)]
        len_total = len(total)

        key = kwargs["key"]
        try:
            assert len({i in total for i in key}) == 1
        except AssertionError:
            print("Ensure all key characters are printable ASCII")
        len_key = len(key)

        text = ""
        for i, char in enumerate(msg):
            # Return same character if it's not printable ASCII
            if char not in total:
                text += char
            else:
                # Find the exact key character in repeating key
                # e.g attackatdawn-->LEMONLEMONLE
                # i.e w == L
                k = key[i % len_key]

                # Index of character and key
                char_id = total.index(char)
                key_id = total.index(k)

                text += (total[(char_id + (sign*key_id)) % len_total])
        return text

    def encrypt(self, msg: str, *args, **kwargs) -> str:
        """Encrypt plaintext to ciphertext using key"""
        return self._implement(msg=msg, sign=1, *args, **kwargs)

    def decrypt(self, ciphertext: str, *args, **kwargs) -> str:
        """Decrypt ciphertext to plaintext using key"""
        return self._implement(msg=ciphertext, sign=-1, *args, **kwargs)
