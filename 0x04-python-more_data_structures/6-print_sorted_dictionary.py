#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for num in sorted(a_dictionary):
        print("{}: {}".format(num, a_dictionary[num]))
