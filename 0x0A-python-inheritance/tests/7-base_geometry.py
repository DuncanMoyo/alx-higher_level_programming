#!/usr/bin/python3

"""class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """base class"""

    def area(self):
        """area raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate input integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
