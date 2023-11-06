#!/usr/bin/python3
"""
is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """ True if obj is an instance or inher from a_class
     false otherwise
    """
    return isinstance(obj, a_class)
