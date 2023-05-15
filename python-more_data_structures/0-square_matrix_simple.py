#!/usr/bin/python3
# Write a function that computes the square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    return [[j ** 2 for j in i] for i in matrix]
