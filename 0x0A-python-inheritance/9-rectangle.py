#!/usr/bin/python3
""" This module contains the definition of class Rectangle..
"""

class New():

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class Rectangle.
    """
    def __init__(self, width, height):
        """ Constructor of the Rectangle instances.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """ returns the string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
