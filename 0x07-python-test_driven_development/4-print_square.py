#!/usr/bin/python3
"""
    Module for print_square method.

"""


def print_square(size):
    """
    Method for Printing a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        for x in range(size):
            print("#", end="")
        print()
