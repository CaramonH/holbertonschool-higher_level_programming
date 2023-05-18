#!/usr/bin/python3
"""this is a square class that defines a square :)"""


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
        """this gives the area of a square"""
        return (self.__size**2)

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """this prints in stdout the square with a special character"""
        if self.__size == 0:
            print("")
        else:
            for t in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print("")
