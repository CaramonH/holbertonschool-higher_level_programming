#!/usr/bin/python3
# Write a function that prints all integers of a list, in reverse order.
# Prototype: def print_reversed_list_integer(my_list=[]):
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for element in reversed(my_list):
            print("{:d}".format(element))
