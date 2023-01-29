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

    def area(self):
        """Returns the area of the Square object.

        Args:
            None.

        Returns:
            The area of the Square instance.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __ne__(self, square_2):
        return self.size != square_2.size

    def __eq__(self, square_2):
        return self.size == square_2.size

    def __lt__(self, square_2):
        return self.size < square_2.size

    def __gt__(self, square_2):
        return self.size > square_2.size

    def __le__(self, square_2):
        return self.size <= square_2.size

    def __ge__(self, square_2):
        return self.size >= square_2.size
