#!/usr/bin/python3

for alphabet in range(122, 96, -1):
    print('{}'.format(chr(alphabet - 32) if alphabet % 2 else chr(alphabet)),
          end="")
