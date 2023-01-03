#!/usr/bin/python3

for num in range(0, 100):
    if not num == 99:
        print('{0:02d}, '.format(num), end="")
    else:
        print('{0:02d}'.format(num), end="\n")
