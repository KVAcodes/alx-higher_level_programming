#!/usr/bin/python3
"""
contains the add_integer function that demonstrates TDD.
"""


def add_integer(a, b=98):
    """adds 2 integers
    Args:
        a (int, float): The first parameter.
        b (int, float): The second parameter.

    Returns:
        int: int(a) + int(b).

    Raises:
        TypeError: if a or b is not an integer
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif a == float('inf') or b == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    elif a == float('nan') or b == float('nan'):
        raise ValueError("cannot convert float NaN to integer")

    return (int)(a) + (int)(b)
