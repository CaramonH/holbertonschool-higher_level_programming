#!/usr/bin/python3
""" 4-from_json_string Module """
import json


def from_json_string(my_str):
    """Return Python object rep of a JSON string."""
    return json.loads(my_str)
