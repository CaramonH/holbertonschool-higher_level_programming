#!/usr/bin/python3
"""Base Class"""


class Base():
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is None:
            Base.__nb_objects += 1
        self.id = Base.__nb_objects if id is None else id
