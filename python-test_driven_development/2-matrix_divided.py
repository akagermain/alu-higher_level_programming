#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int or float): the number to divide every element by.

    Returns:
        list: a new matrix with every element divided by div and
            rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of integers or
            floats, if the rows of matrix are not all the same
            size, or if div is not an integer or a float.
        ZeroDivisionError: if div is equal to 0.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not all(
            isinstance(row, list) and len(row) > 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)) or isinstance(item, bool):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrix
