#!/usr/bin/python3
"""
This module contains the 'matrix_divided' function.
"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix by div

    Args:
        matrix (list): matrix.
        div (int, float): divisor of dividend matrix.

    Returns:
        list: a new quotient matrix of the division.

    Raises:
        TypeError:
            1. If matrix is not a list of lists of integers
            or floats
            2. If each row of the matrix is not of the same
            size.
            3. If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        if not type(row) == list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
