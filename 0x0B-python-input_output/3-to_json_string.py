#!/usr/bin/python3
"""This module contains the to_json_string function definition.
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    """
    if my_obj:
        return json.dumps(my_obj)
