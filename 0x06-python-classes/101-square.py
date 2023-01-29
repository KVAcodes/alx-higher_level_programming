#!/usr/bin/python3

"""This module contains the definition of the Class Square.
"""


class Square:
    """This class defines a Square object as best a possible.
    """
    def __init__(self, size=0, position=(0, 0)):
        """The constructor method of the Square instances.

        Args:
            size (int): The size of the Square object.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        self.position = position

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
        """getter and setter for the size property.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter and setter for the position property/
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) == tuple and len(value) == 2:
            for val in value:
                if type(val) == int and val >= 0:
                    continue
                else:
                    raise TypeError("position must be a tuple of 2 positive \
integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the Square object in a graphical format using
        the '#' character.

        Args:
            None
        Returns:
            None
        """
        if (self.size == 0):
            print()
            return
        for ver in range(self.position[1]):
            print()
        for col in range(self.size):
            for hor in range(self.position[0]):
                print(' ', end="")
            for row in range(self.size):
                print("#", end="")
            print()
        return

    def __str__(self):
        """The string representation of the object instance.
        """
        ret = ""
        if (self.size == 0):
            ret += ""
            return ret
        for ver in range(self.position[1]):
            ret += "\n"
        for col in range(self.size):
            for hor in range(self.position[0]):
                ret += " "
            for row in range(self.size):
                ret += "#"
            ret += "\n" if col < self.size - 1 else ""
        return ret
