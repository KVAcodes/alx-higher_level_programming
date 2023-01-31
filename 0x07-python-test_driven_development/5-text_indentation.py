#!/usr/bin/python3
"""
This module contains the text_indentation function
"""


def text_indentation(text):
    """indents a text."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    index = 0
    while index < len(text):
        print(text[index], end="")
        if text[index] in ['.', '?', ':']:
            print('\n')
            if text[index + 1] == ' ':
                while text[index + 1] == ' ' and index < len(text):
                    index += 1
        index += 1
