#!/usr/bin/python3
""" This module contains the lookup function definition.
"""


def lookup(obj):
    """ return the list of available attributes and methods
    of an object "obj".
    """
    return dir(obj)
