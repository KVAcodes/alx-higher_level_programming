#!/usr/bin/python3

def uppercase(str):

    for letter in str:
        print('{}'.format(chr(ord(letter) - 32) if 97 <= ord(letter) <= 122
                          else letter), end="")
    print(''.format())
