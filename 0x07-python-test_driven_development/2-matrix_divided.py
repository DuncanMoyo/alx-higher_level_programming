#!/usr/bin/python3

"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the division.
    """

    """Check if matrix is a valid matrix of integers/floats"""
    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            isinstance(ele, int) or isinstance(ele, float)
            for ele in [num for row in matrix for num in row]
        )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    """ Check if all rows in the matrix have the same size"""
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """Check if div is a valid number"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """"Check for division by zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Perform the division and round the result to two decimal places"""
    return [
        [round(num / div, 2) for num in row]
        for row in matrix
    ]
