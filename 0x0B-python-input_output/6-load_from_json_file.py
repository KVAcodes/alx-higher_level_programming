#!/usr/bin/python3
"""This module contains the load_from_json_file function definition.
"""


import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".
    """
    if filename:
        with open(filename, "r") as my_file:
            return json.load(my_file)
