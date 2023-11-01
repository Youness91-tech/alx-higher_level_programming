#!/usr/bin/python3
"""

Module for text_indentation method.

"""


def text_indentation(text):
    '''
    Method for adding 2 new lines after each ".", "?", or ":"
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cntr = 0
    while cntr < len(text) and text[cntr] == ' ':
        cntr = cntr + 1

    while cntr < len(text):
        print(text[cntr], end="")
        if text[cntr] == "\n" or text[cntr] in ".?:":
            if text[cntr] in ".?:":
                print("\n")
            cntr = cntr + 1
            while cntr < len(text) and text[cntr] == ' ':
                cntr = cntr + 1
            continue
        cntr = cntr + 1
