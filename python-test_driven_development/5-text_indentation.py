#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_line = True

    for char in text:
        if char != ' ' or new_line is False:
            print(char, end='')
            new_line = False
        elif char != ' ':
            new_line = False

        if char in ['.', '?', ':']:
            print()
            print()
            new_line = True
