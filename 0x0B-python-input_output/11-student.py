#!/usr/bin/python3

"""class Student that defines a student by: (based on 10-student.py)"""


class Student:
    """Defining a student"""

    def __init__(self, first_name, last_name, age):
        """Initialization of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of a student"""
        if (type(attrs) == list and all(type(element) == str
            for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
