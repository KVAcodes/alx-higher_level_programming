#!/usr/bin/python3
"""This module contains the append_write function definition.
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns the number
    of characters added.
    """
    if filename:
        with open(filename, "a") as my_file:
            return my_file.write(text)
