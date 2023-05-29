#!/usr/bin/python3
""" 5-save_to_json_file Module """
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON."""
    with open(filename, "w") as f:
        json.dumps(my_obj)
