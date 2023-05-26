#!/usr/bin/python3
"""Defines a base geometry class"""


class BaseGeometry:
    """Class base"""

    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): name of parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If not an integer
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
