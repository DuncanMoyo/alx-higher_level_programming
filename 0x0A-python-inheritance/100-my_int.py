#!/usr/bin/python3
"""class MyInt inherits from int"""


class MyInt(int):
    """
        Inverts operators
    """

    def __eq__(self, other):
        """!= instead of =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """== instead of !="""
        return super().__eq__(other)
