#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    running_max = my_list[0]
    for integer in my_list:
        if integer > running_max:
            running_max = integer
    return running_max
