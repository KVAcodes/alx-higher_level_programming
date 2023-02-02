#!/usr/bin/python3
"""This module contains the definition of the print_square function.
"""


def print_square(size):
    """Prints a square of size "size" with the character '#'.

    Args:
        size (int): size length of the square.

    Returns:
        None
    Raises:
        TypeError: if size is not an integer and if size is a
            float and is less than zero.
        ValueError: if size is less than zero.
    """

    if size == 0:
        print()
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        for x in range(size):
            print('#', end="")
        print()
