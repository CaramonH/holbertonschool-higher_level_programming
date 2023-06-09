#!/usr/bin/python3
"""Write a class that defines a square:"""


class Square:
    """this class defines a square"""
    def __init__(self, size=0):
        """this initializes a simple square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of the square"""
        return(self.__size**2)

    @property
    def size(self):
        return(self.__size)
