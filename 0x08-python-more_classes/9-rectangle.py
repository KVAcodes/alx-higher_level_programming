#!/usr/bin/python3
"""This module contains the definition of the class Rectangle.
"""


class Rectangle:
    """Defines the attributes of the Rectangle and it's instances.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor of the Rectangle instances.

        Args:
            width (int): width of the rectangle instance.
            height (int): height of the rectangle instance.

        Returns:
            None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter and setter property for the width private instance attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter property for the height private instance
        attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of the rectangle.
        """
        string = ""
        if self.height == 0 or self.width == 0:
            return string
        for y in range(self.height):
            for x in range(self.width):
                string += str(self.print_symbol)
            string += '\n' if y != (self.height - 1) else ""
        return string

    def __repr__(self):
        """Returns a string representatio of the rectangle to
        be able to recreate a new instance by using eval().
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Executes when an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): first rect_1
            rect_2 (Rectangle): second rect_2

        Returns:
            Rectangle: The rectangle with the larger area or rect_1
                if they have equal area.

        Raises:
            TypeError: when rect_1 or rect_2 is not an instance of
                Rectangle
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size.
        """
        new_instance = Rectangle(size, size)
        return new_instance
