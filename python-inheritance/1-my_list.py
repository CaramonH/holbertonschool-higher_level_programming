#!/usr/bin/python3
"""
A module that prints a list in ascending order
"""


class MyList(list):
    def print_sorted(self):
        if issubclass(MyList, list):
            print(sorted(self))
