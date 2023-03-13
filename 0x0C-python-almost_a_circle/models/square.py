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
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
            else:
                return

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.width = kwargs["size"]
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
