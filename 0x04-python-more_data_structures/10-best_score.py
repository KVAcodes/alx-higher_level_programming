#!/usr/bin/python

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    running_max = 0
    key_max = None
    for key, val in a_dictionary.items():
        if val > running_max:
            running_max = val
            key_max = key
    return key_max
