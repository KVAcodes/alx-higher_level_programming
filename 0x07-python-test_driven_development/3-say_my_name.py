#!/usr/bin/python3
"""This module contains the definition of the function say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name (str): the first name.
        last_name (str): the last name.

    Returns:
        None

    Raises:
        TypeError: when either or neithe the first_name and
            last_name are strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
