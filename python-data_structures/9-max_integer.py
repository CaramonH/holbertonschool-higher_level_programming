#!/usr/bin/python3
# Write a function that finds the biggest integer of a list.
# Prototype: def max_integer(my_list=[]):


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
