#!/usr/bin/python3
"""This module contains the save_to_json_file function definition.
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation.
    """
    if filename:
        with open(filename, "w") as my_file:
            json.dump(my_obj, my_file)
