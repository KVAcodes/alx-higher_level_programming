#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    flag = 0
    for row in matrix:
        for item in row:
            if flag == 0:
                print("{:d}".format(item), end="")
                flag = 1
            else:
                print(" {:d}".format(item), end="")
        print()
        flag = 0
    return
