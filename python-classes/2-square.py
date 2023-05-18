#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """this class defines Square"""
    def __init__(self, size=0):
        """this initializes a simple square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
