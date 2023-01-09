#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        temp_str = ''
        for letter in my_string:
            if letter not in 'cC':
                temp_str += letter
        return temp_str
    return my_string
