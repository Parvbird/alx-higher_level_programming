#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    square value of all integers of a matrix

    Args:
        matrix: 2D array of integers

    Return: the squared matrix
    """
    new_matrix = [[element ** 2 for element in row] for row in matrix]
    return new_matrix
