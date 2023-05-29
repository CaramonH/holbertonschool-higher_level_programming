#!/usr/bin/python3
""" 3-to_json_string Module """
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
