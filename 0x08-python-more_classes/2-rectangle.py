#!/usr/bin/python3

"""class Rectangle that defines a rectangle by: (based on 1-rectangle.py)"""


class Rectangle:
    """Defining the characteristics of a rectangle"""
    def __init__(self, width=0, height=0):
        """
        Defining attributes of the rectangle

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        width property setter

        Args:
        value (int): integer value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        height property setter

        Args:
        value (int): integer value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculating the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculating the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
