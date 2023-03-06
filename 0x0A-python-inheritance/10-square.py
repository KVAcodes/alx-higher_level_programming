#!/usr/bin/python3
""" This module contains the definition of class Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square.
    """
    def __init__(self, size):
        """ Constructor of the Square instances.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """ returns a string representation of the square.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
