#!/usr/bin/python3

"""This module contains the definition of the add_integer function.
"""


def add_integer(a, b=98):
    """
    This function returns the addition of two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float): The second integer or float.

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if a or b is not a Float or Integer.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
