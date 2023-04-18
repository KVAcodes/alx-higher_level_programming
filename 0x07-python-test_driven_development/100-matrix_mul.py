#!/usr/bin/python3
"""This module contains the definition of the matrix_mul function.
"""


def matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices if they are valid matrices
    and if matrix multiplication is possible.

    Args:
        m_a (list(list)): matrix a
        m_b (list(list)): matrix b

    Returns:
        List: The resulting matrix.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for lst in m_a:
        if type(lst) != list:
            raise TypeError("m_a must be a list of lists")
    for lst in m_b:
        if type(lst) != list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for lst in m_a:
        for elem in lst:
            if type(elem) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for lst in m_b:
        for elem in lst:
            if type(elem) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    length = len(m_a[0])
    for lst in m_a:
        if length != len(lst):
            raise TypeError("each row of m_a must be of the same size")
    length = len(m_b[0])
    for lst in m_b:
        if length != len(lst):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for lst in m_a:
        index = 0
        nthRow = []
        while index != len(m_b):
            m_b_vert = [lst_1[index] for lst_1 in m_b]
            elem = sum([lst[idx] * m_b_vert[idx] for idx in range(len(m_b))])
            nthRow.append(elem)
            index += 1
        result.append(nthRow)
    return result
