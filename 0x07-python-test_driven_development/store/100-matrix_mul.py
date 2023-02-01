#!/usr/bin/python3
"""This module contains the matrix_mul function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list of lists of ints or floats): first matrix argument.
        m_b (list of lists of ints or floats): second matrix argument.

    Raises:
        TypeError: If either argument is not a list/ if either argument
        is not a list of lists/ if either argument is doesn't contain only
        integer and floats.
        ValueError: If either argument is empty/ if the matrices can't be
        multiplied due to (m_a no of columns not == m_b no of rows).

    Returns:
        a new matrix that represents the multiplication of m_a and m_b.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    index = 0
    while index < len(m_a):
        if not len(m_a[index]) == len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        index += 1
    index = 0
    while index < len(m_b):
        if not len(m_b[index]) == len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        index += 1
    m_a_col_no = 0
    m_b_row_no = 0
    for col in m_a[0]:
        m_a_col_no += 1
    for row in m_b:
        m_b_row_no += 1
    if not m_a_col_no == m_b_row_no:
        raise ValueError("m_a and m_b can't be multiplied")
    # Transposing matrix m_b
    m_b = [[row[i] for row in m_b] for i in range(len(m_b[0]))]

    return [[sum([row_a[i] * row_b[i] for i in range(len(m_a[0]))])
             for row_b in m_b] for row_a in m_a]
