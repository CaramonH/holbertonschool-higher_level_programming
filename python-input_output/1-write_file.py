#!/usr/bin/python3
""" 1-write_file Module """


def write_file(filename="", text=""):
    """Writes a string to a text file and returns character count"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
