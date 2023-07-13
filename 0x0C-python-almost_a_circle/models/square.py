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

    def update(self, *args, **kwargs):
        """This will assign to each attribute"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
