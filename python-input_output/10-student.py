#!/usr/bin/python3
""" 10-student Module """


class Student:
    """ Class describes a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary representation of a Student instance """
        if attrs is None:
            return cars(self)
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = vars(self)[i]
            except Exception:
                pass
        return new_dict
