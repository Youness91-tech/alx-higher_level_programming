#!/usr/bin/python3

"""
This Module adds two integers.
"""


def add_integer(a, b=98):

    """
    add_integer: adds two integers together and checks if the intput is right
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
