#!/usr/bin/python3
""" 2-append_write Module """


def append_write(filename="", text=""):
    """Writes a string to file end and returns character count"""
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
