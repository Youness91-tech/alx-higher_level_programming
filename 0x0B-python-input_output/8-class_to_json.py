#!/usr/bin/python3
"""class_to_json module"""


def class_to_json(obj):
    """a function that returns the dictionary description"""
    return obj.__dict__
