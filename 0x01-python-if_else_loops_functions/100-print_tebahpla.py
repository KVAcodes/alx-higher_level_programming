#!/usr/bin/python3

for lt in range(122, 96, -1):
    print("{0}".format(chr(lt) if lt % 2 == 0 else chr(lt - 32)), end="")
