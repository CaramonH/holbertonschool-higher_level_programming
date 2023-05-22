#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """
    This function prints a square with #.

    Args:
        size: size of square

    Raises:
        TypeError if size is not int
        ValueError is size < 0
        TypeError if size < 0 and is not an integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
