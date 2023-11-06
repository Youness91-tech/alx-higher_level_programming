#!/usr/bin/python3
""""add_attribute module"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
