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
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        """
        for offset in range(self.__y):
            print()
        for row in range(self.__height):
            for offset in range(self.__x):
                print(' ', end='')
            for col in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """returns the string representation of the the rectangle object.
        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"
            f" {self.__width}/{self.__height}"
               )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute.

        Args:
            args (list of int): updated arguments
        Returns:
            None
        """
        if len(args):
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                return
            else:
                return

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
