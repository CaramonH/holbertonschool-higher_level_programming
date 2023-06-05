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

    @property
    def size(self):
        """ Getter for size of Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size of Square """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ Public instance method that returns the dictionary
        representation of Square """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def update(self, *args, **kwargs):
        """ Public method that updates or assigns attributes. """
        attributes = ['id', 'size', "x", "y"]

        if args and len(args) > 0:
            for index, value in enumerate(args):
                if index < len(attributes):
                    if attributes[index] == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, attributes[index], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    if key == "size":
                        self.width = value
                        self.height = value
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """ Overloading the __str__ method for the Square class """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )
