#!/usr/bin/python3

class LockedClass:
    __slots__ = []

    def __setattr__(self, attr, value):
        if hasattr(self, attr):
            super().__setattr__(attr, value)
        elif attr = 'first_name':
            super().__setattr__(attr, value)
        else:
            raise AttributeError("Cannot create new instance attributes")
