#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = None
        div = a / b
    except ZeroDivisionError:
        return None
    else:
        return div
    finally:
        print("Inside result: {}".format(div))
