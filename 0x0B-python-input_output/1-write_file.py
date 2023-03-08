#!/usr/bin/python3
"""This module contains the definition of the function write_file.
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the number of
    characters written
    """
    if filename:
        with open(filename, 'w') as my_file:
            return my_file.write(text)
