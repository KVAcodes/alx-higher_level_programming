#!/usr/bin/python3
"""This module contains the definition of the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """matrix_divided divides matrix "matrix" by integer or float "div".

    Args:
        matrix (list): The matrix as a list of lists
        div (int or float): The integer or float value to divided through by

    Returns:
        list: a new matrix

    Raises:
        TypeError: if the matrix is not a list of ints or floats, if each row
        of the matrix are not of the same size and if div is not a float or
        int.
        ZeroDivisionError: if div is zero.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if len(matrix) == 0:
        return []
    length = len(matrix[0])

    for lst in matrix:
        if type(lst) != list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(lst) != length:
            raise TypeError("Each row of the matrix must have the same size")

    for lst in matrix:
        for elem in lst:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    return [[round(elem / div, 2) for elem in lst] for lst in matrix]
