#!/usr/bin/python3
"""This module contains the definition of text_indentation function.
"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (str): the text

    Returns:
        None

    Raises:
        TypeError: when text is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    index = 0
    while index in range(len(text)):
        if text[index] in ['.', '?', ':']:
            print(text[index], end="")
            print()
            print()
            index += 2 if text[index + 1] == ' ' else 1
            continue
        else:
            print(text[index], end="")
            index += 1
