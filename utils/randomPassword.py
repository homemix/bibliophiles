import string
from random import choice


def random_password(length=5):
    """
    Generates a random password of length 5 by default.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(choice(chars) for i in range(length))
