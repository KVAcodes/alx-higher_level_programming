#!/usr/bin/python3
"""This module contains the definition of class Base.
"""


class Base:
    """ The Base Class, the base of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor of the Base class.

        Args:
            id (int): the id of Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
