#!/usr/bin/python3
"""Contains the find_peak function definition.
"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of
    unsorted integers.
    """
    if not list_of_integers:
        return
    start, end = 0, len(list_of_integers) - 1
    centre = (end + start) // 2 + 1

    if end == 0:
        return list_of_integers[start]
    return max(find_peak(list_of_integers[start:centre]),
               find_peak(list_of_integers[centre:]))
