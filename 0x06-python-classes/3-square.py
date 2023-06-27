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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculates the area of a square"""

        return self.__size ** 2
