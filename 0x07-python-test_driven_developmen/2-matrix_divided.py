#!/usr/bin/python3

'''This module contains a function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''
    Function that divides all elements of a matrix.

    Args:
        matrix: matrix to be divided
        div: number to divide the matrix by

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats or if
                   div is not an integer or float.
        ZeroDivisionError: If div is equal to 0.

        Returns:
            A new matrix with the result of the division.
    '''
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [number for row in matrix for number in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
