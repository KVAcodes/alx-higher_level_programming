#!/usr/bin/python3
""" This module contains the read_file function definition.
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout.
    """
    if filename:
        with open(filename, 'r') as my_file:
            print(my_file.read(), end='')
