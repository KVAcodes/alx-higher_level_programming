#!/usr/bin/python3
"""Contains the find_peak function definition.
"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of
    unsorted integers.
    """
    if list_of_integers:
        list_of_integers.sort()
    else:
        return
    return list_of_integers[-1]
