#!/usr/bin/python3
""" This module defines the class Base """

import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor for Base class """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that Returns: the JSON string representation
        of a list of dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Static method that Returns: the list of the JSON string """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method writes the JSON representation of a string to a file"""
        filename = cls.__name__ + ".json"
        if not list_objs:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(list_dicts)
        with open(filename, "w") as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance of a class """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that Returns: A list of instances. """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
                return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []
