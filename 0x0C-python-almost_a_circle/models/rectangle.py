#!/usr/bin/python3
"""This module contains the defintion of Rectangle class.
"""


from models.base import Base


class Rectangle(Base):
    """The Rectangle object sub class of Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer/Constructor for the Rectangle class instances.

        Args:
            width (int): width of the rectangle object.
            height (int): height of the rectangle object.
            x (int): position on the x-axis.
            y (int): position on the y-axis.
            id (int): id.

        Returns:
            None

        Raises:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets/sets the width of the rectangle."""
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
        """Gets/sets the height of the rectangle."""
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
        """Gets/sets the x position of the rectangle."""
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
        """Gets/sets the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
