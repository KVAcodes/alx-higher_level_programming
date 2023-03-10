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

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance.
        """
        if attrs is not None:
            ret = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    ret.update({key: value})
            return ret
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance using the dict
        json's keys and values.
        """
        for key, value in json.items():
            self.__dict__.update({key: value})
