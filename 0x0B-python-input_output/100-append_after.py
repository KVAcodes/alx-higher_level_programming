#!/usr/bin/python3
"""This module contains the append_after function definition
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing a specific
    string.
    """
    if filename:
        with open(filename, "r+") as my_file:
            old_content = my_file.readlines()
            new_input = []
            for idx in range(len(old_content)):
                if old_content[idx].find(search_string) == -1:
                    new_input.append(old_content[idx])
                else:
                    new_input.append(old_content[idx])
                    new_input.append(new_string)
            my_file.seek(0)
            my_file.write("".join(new_input))
