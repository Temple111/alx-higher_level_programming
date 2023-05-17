#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_uare = []
    for similarities in matrix:
        sq_uare.append([b**2 for b in similarities])
    return sq_uare
