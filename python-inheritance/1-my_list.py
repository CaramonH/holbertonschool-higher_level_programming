#!/usr/bin/python3
"""A module that prints a list in ascending order"""


class MyList(list):
    """Implements sorted printing for list class"""

    def print_sorted(self):
        if issubclass(MyList, list):
            print(sorted(self))
