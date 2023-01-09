#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    counter = 1
    final_sum = 0
    while counter < len(argv):
        final_sum += int(argv[counter])
        counter += 1
    print('{}'.format(final_sum))
