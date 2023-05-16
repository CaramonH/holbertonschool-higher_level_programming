#!/usr/bin/python3
# Write a function that prints the first x elements of a list
# and only integers.


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
