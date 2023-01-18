#!/usr/bin/python3

def uppercase(str):
    for lt in str:
        print("{0}".format(chr(ord(lt) - 32)) if ord(lt) > 96 and ord(lt) < 123
              else "{0}".format(lt), end="")
    print()
