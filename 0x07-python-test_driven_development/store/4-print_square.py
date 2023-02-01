#!/usr/bin/python3
"""
This module contains the print_square function
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): Size of square.

    Returns:
        None

    Raises:
        TypeError: if size is not an int.
        ValueError: if size is less than zero.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for char in range(size):
            print("#", end="")
        print()
