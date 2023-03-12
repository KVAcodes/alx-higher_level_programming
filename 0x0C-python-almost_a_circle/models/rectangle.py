#!/usr/bin/python3
"""This module contains the Rectangle class definition.
"""
from .base import Base


class Rectangle(Base):
    """This is the Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of the Rectangle object instances.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int): position of the rectangle on the X axis.
            y (int): position of the rectangle on the Y axis.
            id (None): id of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter and setter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter and setter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter and setter for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter and setter for the x attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self__y = value
