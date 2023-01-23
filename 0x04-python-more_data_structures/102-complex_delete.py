#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key, test in a_dictionary.items():
        if test == value:
            keys_to_delete.append(key)
    for keys in keys_to_delete:
        del a_dictionary[keys]
    return a_dictionary
