#!/usr/bin/python3
""" Module for say_my_name method. """


def say_my_name(first_name, last_name=""):
    """ Method for printing first and last name
    names must be strings otherwise, raise a TypeError,
    first_name must be a string or last_name must be a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
