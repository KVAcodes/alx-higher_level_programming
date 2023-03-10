#!/usr/bin/python3
"""This module contains the Student class defintion.
"""


class Student:
    """The Student class.
    """
    def __init__(self, first_name, last_name, age):
        """Constructor of the Student instances.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
