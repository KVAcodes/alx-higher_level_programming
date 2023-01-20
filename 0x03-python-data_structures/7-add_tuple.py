#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        while len(tuple_a) < 2:
            tuple_a += (0, )
    if len(tuple_b) < 2:
        while len(tuple_b) < 2:
            tuple_b += (0, )
    added_tuple = ()
    for i in range(2):
        added_tuple += (tuple_a[i] + tuple_b[i],)
    return added_tuple
