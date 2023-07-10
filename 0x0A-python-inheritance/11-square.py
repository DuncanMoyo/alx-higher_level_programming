#!/usr/bin/python3

"""
    class Square that inherits from Rectangle (9-rectangle.py).
    (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square defined"""

    def __init__(self, size):
        """squre intialisesd"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
