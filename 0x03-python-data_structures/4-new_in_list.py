#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    temp_list = []
    for elem in my_list:
        temp_list.append(elem)
    temp_list[idx] = element
    return temp_list
