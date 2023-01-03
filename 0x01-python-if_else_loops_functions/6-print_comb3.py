#!/usr/bin/python3

for digit_2 in range(0, 10):
    for digit_1 in range(0, 10):
        if digit_2 == digit_1:
            continue
        if not digit_2 == digit_1:
            if digit_2 > digit_1:
                continue
            else:
                num = (digit_2 * 10) + digit_1
                if num == 89:
                    print('{:02d}'.format(num), end="\n")
                else:
                    print('{:02d}, '.format(num), end="")
