#!/usr/bin/python3
"""This a program That solves the N queens problem.
"""


import sys

def board_init(n):
    """Creates a n by n board as a 2-D list and
    initializes the whole board with "None" and
    Returns the board for further analysis.
    """
    return [[None for x in range(n)] for y in range(n)]

def isValid(board, row, column, n):
    """Checks if the square is being attacked by any queens on the
    board as at the time in question.
    """
    # row check
    for x in board[row]:
        if not x is None:
            return False
    # col check
    for y in [lst[column] for lst in board]:
        if not y is None:
            return False
    # Diagonals check
        # For Negative slope diag
    tmp_row = row
    tmp_col = column

    while tmp_row >= 0 and tmp_col >= 0:
        tmp_row -= 1
        tmp_col -= 1
        if board[tmp_row][tmp_col] is True:
            return False
        else:
            continue

    tmp_row = row
    tmp_col = column

    while tmp_row != n - 1 and tmp_col != n - 1:
        tmp_row += 1
        tmp_col += 1
        if board[tmp_row][tmp_col] is True:
            return False
        else:
            continue

    tmp_row = row
    tmp_col = column

    while tmp_row >= 0 and tmp_col != n - 1:
        tmp_row -= 1
        tmp_col += 1
        if board[tmp_row][tmp_col] is True:
            return False
        else:
            continue

    tmp_row = row
    tmp_col = column

    while tmp_row != n -1 and tmp_col >= 0:
        tmp_row += 1
        tmp_col -= 1
        if board[tmp_row][tmp_col] is True:
            return False
        else:
            continue
    return True

def trackback(board, row_index, n):
    """
