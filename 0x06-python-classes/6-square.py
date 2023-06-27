#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """The square"""

    def __init__(self, size=0, position=(0, 0)):
        """instantiate a new square

        Args:
        size (int): the size of the new square
        position (int, int): position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter

        Args:
        value (int): the vlue for the size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter

        Args:
            value (tuple): set of 2 positive integers representing the position

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(val, int) for val in value) or \
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
