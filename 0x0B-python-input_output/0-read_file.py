#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)"""
    with open(filename, encoding="UTF8") as f:
        line = f.read()
    print(line, end="")
    f.close()
