#!/usr/bin/python3
""" finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """Find a peak in a list"""
    if list_of_integers == []:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        middle = (left + right) // 2

        if list_of_integers[middle] > list_of_integers[middle + 1]:
            right = middle
        else:
            left = middle + 1

    return list_of_integers[left]
