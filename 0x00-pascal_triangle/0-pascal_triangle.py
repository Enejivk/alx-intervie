#!/usr/bin/python3

def pascal_triangle(n):
    matrix = []
    if n <= 0:
        return matrix
    
    for i in range(n):
        inner_list = []
        for j in range(i + 1 ):
            if j == 0 or j == i:
                inner_list.append(1)
            else:
                inner_list.append(matrix[i-1][j-1] + matrix[i-1][j])
        matrix.append(inner_list)
    return matrix