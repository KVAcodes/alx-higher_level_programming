#!/usr/bin/python3
"""This module contains the definition of the class Square.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the class Square, inherits from the Rectangle and Base classes.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer/Constructor of the Square class.

        Args:
            size (int): width/height of the Square object.
            x (int): position in the x-axis.
            y (int): position in the y-axis.
            id (int): id of the Square object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation for a Square object.
        """
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )

    @property
    def size(self):
        """Getter and Setter for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
