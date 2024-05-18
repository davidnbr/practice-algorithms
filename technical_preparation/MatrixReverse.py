#!/bin/python3

import math
import os

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.

def revColumn(Matrix, col_num):
    for i in range(len(Matrix[0])//2):

        Matrix[i][col_num], Matrix[len(Matrix[0])-i-1][col_num] = Matrix[len(Matrix[0])-i-1][col_num], Matrix[i][col_num]
    
    return Matrix
    
def revRow(Matrix, row_num):
    for j in range(len(Matrix)//2):
        Matrix[row_num][j], Matrix[row_num][len(Matrix[0])-j-1] = Matrix[row_num][len(Matrix[0])-j-1], Matrix[row_num][j]
    
    return Matrix

def subSum(matrix):
    sum_ = 0
    for i in range(len(matrix)//2):
        for j in range(len(matrix[0])//2):
            sum_ += (matrix[i][j])
    return sum_

def flippingMatrix(matrix):
    sorted_values = []
    sum_ = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sorted_values.append(matrix[i][j])
    sorted_values.sort(reverse=True) # Ordenar en forma ascendente por defecto, colocar reverse=True para ordenar en forma descendente
    
    for value in sorted_values:

        for row in range(len(matrix)):
            try:
                index = matrix[row].index(value)
                
                if index>0:

                    if (matrix[row][index-1]+matrix[row][index])<(matrix[-row-1][index-1]+matrix[row][index]):
                        _sum = subSum(matrix)
                        matrix = revColumn(matrix, (index-1))

                        if subSum(matrix) < _sum:
                            matrix = revColumn(matrix, (index-1))

                if index<len(matrix)-1:

                    if (matrix[row][index+1]+matrix[row][index])<(matrix[-row-1][index+1]+matrix[row][index]):
                        _sum = subSum(matrix)
                        matrix = revColumn(matrix, (index+1))
                        if subSum(matrix) < _sum:
                            matrix = revColumn(matrix, (index+1))
            except:
                continue
        
        for column in range(len(matrix[0])):
            try:
                arr = [sub[column] for sub in matrix]

                if column==0:
                    arr = [sub[len(matrix[0])-1] for sub in matrix]
                elif column==len(matrix[0])-1:
                    inv_arr = [sub[0] for sub in matrix]
                else:
                    inv_arr = [sub[-column-1] for sub in matrix]

                index = arr.index(value)

                if index>0:

                    if (arr[index-1]+arr[index])<(inv_arr[index-1]+arr[index]):
                        _sum = subSum(matrix)
                        matrix = revRow(matrix, (index-1))
                        if subSum(matrix) < _sum:
                            matrix = revRow(matrix, (index-1))

                if index<len(matrix[0])-1:
                    der_arr = [sub[column+1] for sub in matrix]

                    if (arr[index+1]+arr[index])<(inv_arr[index+1]+arr[index]):
                        _sum = subSum(matrix)
                        matrix = revRow(matrix, (index+1))
                        if subSum(matrix) < _sum:
                            matrix = revRow(matrix, (index+1))
            except:
                continue

    sum_ = subSum(matrix)
    
    print(f"Final matrix: {matrix}")
    return sum_

if __name__ == '__main__':


    #matrix = [[112, 42, 83, 2], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    
    print(f"Original matrix: {matrix}")
    result = flippingMatrix(matrix)
    print(result)


"""


1
2
112 42 83 119
56 125 56 49
15 78 101 43
62 98 114 108
"""
