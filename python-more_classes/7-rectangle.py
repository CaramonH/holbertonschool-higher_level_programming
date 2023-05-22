#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initiates a new Rectangle.

        Args:
            width (int): width of new rectangle.
            height (int): height of new rectangle.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width > 0 and self.height > 0:
            return (self.width * 2) + (self.height * 2)
        else:
            return 0

    def __str__(self):
        """Print the rectangle with the character #"""
        rectangle = ""
        if (self.__height or self.__width) == 0:
            return rectangle
        for i in range(self.__height):
            for i in range(self.__width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        return ("Rectangle ({}, {})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
