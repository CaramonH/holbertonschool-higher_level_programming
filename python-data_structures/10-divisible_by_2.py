#!/usr/bin/python3
# Write a function that returns the list of numbers divisible by 2.
# Prototype: def divisible_by_2(my_list=[]):


def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
