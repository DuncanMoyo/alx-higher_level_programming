#!/usr/bin/python3

"""class Square that inherits from Rectangle (9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a square with rectangle as a base"""

    def __init__(self, size):
        """"inititialise it"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)
