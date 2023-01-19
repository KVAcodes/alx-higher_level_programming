#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    counter = 1
    added_value = 0
    while not counter == len(argv):
        added_value += int(argv[counter])
        counter += 1
    print(added_value)
