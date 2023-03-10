#!/usr/bin/python3
"""This module contains the from_json_string function definition.
"""

import json


def from_json_string(my_obj):
    """returns the JSON representation of an object (string)
    """
    return json.loads(my_obj)
