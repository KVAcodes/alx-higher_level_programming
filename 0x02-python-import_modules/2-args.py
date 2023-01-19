#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))
    if len(argv) >= 2:
        for num, item in enumerate(argv):
            if num == 0:
                continue
            else:
                print("{} : {}".format(num, item))
