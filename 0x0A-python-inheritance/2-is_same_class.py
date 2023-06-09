#!/usr/bin/python3

"""returns True if the object is exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """checks if an exact instance of a specified class exists"""
    return type(obj) is a_class
