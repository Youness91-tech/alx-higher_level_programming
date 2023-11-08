#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """a func that inserts a line of text to a file,
    fter each line containing a specific string"""
    inserted_text = ""
    with open(filename) as f:
        for line in f:
            inserted_text += line
            if search_string in line:
                inserted_text += new_string
    with open(filename, "w") as r:
        r.write(inserted_text)
