#!/usr/bin/python3

"""class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """
        Initiates a new square.
            Args:
                size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Size property setter

        Args:
            value (int): The value of the size element
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates the area of a square"""

        return self.__size ** 2
