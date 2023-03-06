#!/usr/bin/python3
"""This module contains add_attribute function.
"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it's possible.

    Args:
        obj (object): object in which attribute is to be added.
        attr (str): attribute string.
        value (optional): value contained by attribute.

    Raises:
        TypeError: if the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
