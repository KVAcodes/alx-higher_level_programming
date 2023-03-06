#!/usr/bin/python3
""" This module contains the definition of class BaseGeometry.
"""


class BaseGeometry:
    """ class BaseGeometry.
    """
    def __init__(self, width, height):
        """ Constructor of the BaseGeometry instances.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """raise an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an int.
        """
        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")
        if not value > 0:
            raise ValueError(f"{name} must be greater than 0")
