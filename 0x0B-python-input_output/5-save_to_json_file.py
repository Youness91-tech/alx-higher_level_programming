#!/usr/bin/python3
"""save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """ a funct that writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
