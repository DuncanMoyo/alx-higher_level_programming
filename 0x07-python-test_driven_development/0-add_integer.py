#!/usr/bin/python3

"""a function that adds 2 integers"""


def add_integer(a, b=98):
    """
    Takes two integers of type integer/float and returns
    the total of their addition.

    a and b must be first casted to integers if they are float

    Args:
    a: first integer or float in the summation
    b: second integer or float in the summation

    Return: the addition of the 2 arguments

    Raises: a must be an integer/float or b must be an integer/float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
