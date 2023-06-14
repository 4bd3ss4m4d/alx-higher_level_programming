#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return [[column ** 2 for column in row] for row in matrix]
