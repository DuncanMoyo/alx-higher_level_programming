#!/usr/bin/python3

"""first class Base"""
import json


class Base:
    """
        Base class for all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Constructor
            Args:
                id (int, optional): the id of the object. if not provided an
                id will automatically be assigned
        """
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string
