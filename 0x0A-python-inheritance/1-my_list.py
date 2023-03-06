#!/usr/bin/python3
""" This module contains the definition of the class MyList.
"""


class MyList(list):
    """ A class MyList that inherits from the list class.
    """
    def print_sorted(self):
        print(sorted(self))
