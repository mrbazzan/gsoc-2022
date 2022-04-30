
import re
from argparse import ArgumentTypeError


def non_negative_int(string):
    if not re.fullmatch("[1-9]+", string):
        raise ArgumentTypeError(
            f'{repr(string)} is not a positive integer'
        )
    return int(string)
