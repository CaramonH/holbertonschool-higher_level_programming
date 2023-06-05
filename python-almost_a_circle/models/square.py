#!/usr/bin/python3
"""This module defines the class Square that inherits the Rectangle class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle Class. """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of the Square class that inherits from Rectangle
        """
        super().__init__(size, size, x, y, id)
