#!/usr/bin/python3
"""This module is a script that adds all arguments to a python list, and
then saves them to a file.
"""

import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
to_file = sys.argv[1:]

try:
    from_file = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file(to_file, "add_item.json")
else:
    save_to_json_file(from_file + to_file, "add_item.json")
