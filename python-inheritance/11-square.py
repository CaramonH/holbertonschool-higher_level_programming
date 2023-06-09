#!/usr/bin/python3
"""Defines a Rectangle sublass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation of Rectangle"""
        return "[Square] {}/{}".format(self.__size, self.__size)
