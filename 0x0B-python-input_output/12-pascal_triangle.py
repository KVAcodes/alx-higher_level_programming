#!/usr/bin/python3
"""This module contains the pascal_triangle function definition.
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle
    of n.
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for row in range(0, n - 1):
        tmp = []
        prev = 0
        for elem in triangle[row]:
            tmp.append(elem + prev)
            prev = elem
        tmp.append(1)
        triangle.append(tmp)
    return triangle
