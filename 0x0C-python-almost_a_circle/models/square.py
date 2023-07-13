#!/usr/bin/python3

"""Defining the square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
