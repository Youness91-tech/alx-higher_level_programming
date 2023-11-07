#!/usr/bin/python3
"""student module"""


class Student:
    """a student class"""

    def __init__(self, first_name, last_name, age):
        """init new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for att in attrs:
            if type(att) is not str:
                return self.__dict__
        return {d: self.__dict__[d] for d in self.__dict__ if d in attrs}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
