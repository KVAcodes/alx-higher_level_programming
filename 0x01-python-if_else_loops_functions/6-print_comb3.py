#!/usr/bin/python3

flag = 0
for num_1 in range(0, 10):
    for num_2 in range(0, 10):
        if num_1 >= num_2:
            continue
        else:
            if flag == 0:
                print("{0}{1}".format(num_1, num_2), end="")
                flag = -1
            else:
                print(" ,{0}{1}".format(num_1, num_2), end="")

print()
