#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':
                  1000}
    counter = 0
    integer = roman_dict[roman_string[0]]

    while counter + 1 < len(roman_string):
        next = roman_dict[roman_string[counter + 1]]
        prev = roman_dict[roman_string[counter]]
        if prev < next:
            integer += next - 2 * prev
        else:
            integer += next
        counter += 1
    return integer
