#!/usr/bin/python3
""" This module contains the MyInt class definition.
"""


class MyInt(int):
    """ class MyInt "a rebel int class).
    """
    def __init__(self, val):
        """constructor of the MyInt class.
        """
        super().__init__()
        self.__val = val

    def __eq__(self, num_2):
        """tests equality of MyInt numbers.
        """
        return self.__val != num_2

    def __ne__(self, num_2):
        """tests non-equality of MyInt numbers.
        """
        return self.__val == num_2
