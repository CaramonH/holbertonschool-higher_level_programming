#!/usr/bin/python3
""" 9-student Module """


class Student:
    """ Class describes a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Dictionary representation of a Student instance """
        return vars(self)
