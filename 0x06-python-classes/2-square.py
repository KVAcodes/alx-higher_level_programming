#!/usr/bin/python3

"""This module contains the definition of the Class Square.
"""


class Square:
    """This class defines a Square object as best a possible.
    """
    def __init__(self, size=0):
        """The constructor method of the Square instances.

        Args:
            size (int): The size of the Square object.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
