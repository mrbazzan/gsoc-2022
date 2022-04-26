import abc


class Cipher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def encrypt(self, msg: str, *args, **kwargs) -> str:
        pass

    @abc.abstractmethod
    def decrypt(self, ciphertext: str, *args, **kwargs) -> str:
        pass
