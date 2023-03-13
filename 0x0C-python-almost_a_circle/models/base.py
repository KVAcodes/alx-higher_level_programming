#!/usr/bin/python3
"""This module contains the definition of class Base.
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.
        """
        with open(f"{cls.__name__}.json", "w") as j_file:
            j_file.write(cls.to_json_string([obj.to_dictionary() for obj in
                                             list_objs] if list_objs is not
                                            None else None))

    def from_json_string(json_string):
        """returns the list of the JSON string representation "json_string".
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(0, 0, 0, 0, 0)
        elif cls.__name__ == "Square":
            dummy_instance = cls(0, 0, 0, 0)
        dummy_instance.update(**dictionary)
        return dummy_instance
