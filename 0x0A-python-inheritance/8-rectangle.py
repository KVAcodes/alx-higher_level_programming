#!/usr/bin/python3
""" This module contains the definition of class Rectangle..
"""


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
