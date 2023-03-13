#!/usr/bin/python3
"""This module contains the Rectangle class definition.
"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer/Constructor of the Rectangle object instances.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
            x (int): position of the rectangle on the X axis.
            y (int): position of the rectangle on the Y axis.
            id (None): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter and setter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter and setter for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter and setter for the x attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self__y = value
