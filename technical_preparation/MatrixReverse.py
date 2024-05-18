#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#https://stackoverflow.com/questions/40205519/largest-sum-of-upper-left-quadrant-of-matrix-that-can-be-formed-by-reversing-row
#https://www.geeksforgeeks.org/maximize-sum-n-x-n-upper-left-sub-matrix-given-2n-x-2n-matrix/

def revColumn(Matrix, col_num):
    for i in range(len(Matrix[0])//2):
        #print(Matrix[j][col_num], Matrix[len(Matrix[0])-j-1][col_num])
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
        #print("################################################")
        #print(f"Value: {value}")

        for row in range(len(matrix)):
            try:
                index = matrix[row].index(value)
                #print(f"------------Index: {index}------------")

                #for rrow in matrix:
                    #print(rrow)

                if index>0:
                    #print(matrix[row][index-1], matrix[row][index],matrix[-row-1][index-1])
                    if (matrix[row][index-1]+matrix[row][index])<(matrix[-row-1][index-1]+matrix[row][index]):
                        _sum = subSum(matrix)
                        matrix = revColumn(matrix, (index-1))
                        #print(f"Matrix after revColumn: {matrix}")
                        if subSum(matrix) < _sum:
                            matrix = revColumn(matrix, (index-1))

                if index<len(matrix)-1:
                    #print(matrix[row][index+1], matrix[row][index],matrix[-row-1][index+1])
                    if (matrix[row][index+1]+matrix[row][index])<(matrix[-row-1][index+1]+matrix[row][index]):
                        _sum = subSum(matrix)
                        matrix = revColumn(matrix, (index+1))
                        #print(f"Matrix after revColumn index+1: {matrix}")
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

                #print(f"------------Index: {index}------------")
                #for rrow in matrix:
                    #print(rrow)
                if index>0:
                    #print(f"Columna: {arr}")

                    #print(arr[index-1], arr[index],inv_arr[index-1])
                    if (arr[index-1]+arr[index])<(inv_arr[index-1]+arr[index]):
                        _sum = subSum(matrix)
                        matrix = revRow(matrix, (index-1))
                        #print(f"Matrix after revRow: {matrix}")
                        if subSum(matrix) < _sum:
                            matrix = revRow(matrix, (index-1))

                if index<len(matrix[0])-1:
                    #print(f"Columna: {arr}")
                    der_arr = [sub[column+1] for sub in matrix]

                    #print(arr[index+1], arr[index],inv_arr[index+1])
                    if (arr[index+1]+arr[index])<(inv_arr[index+1]+arr[index]):
                        _sum = subSum(matrix)
                        matrix = revRow(matrix, (index+1))
                        #print(f"Matrix after revRow: {matrix}")
                        if subSum(matrix) < _sum:
                            matrix = revRow(matrix, (index+1))
                        #print(f"Matrix after revRow index+1: {matrix}")
            except:
                continue

        """for i in range(len(matrix)):
            if values in matrix[i]:
                row = i
                col = matrix[i].index(values)
                break
        if row < len(matrix)//2:
            matrix = revRow(matrix, row)
        if col < len(matrix[0])//2:
            matrix = revColumn(matrix, col)"""
    sum_ = subSum(matrix)
    
    print(f"Final matrix: {matrix}")
    return sum_

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input().strip())

    """for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
    """
    #matrix = [[112, 42, 83, 2], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    
    print(f"Original matrix: {matrix}")
    result = flippingMatrix(matrix)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()


"""


1
2
112 42 83 119
56 125 56 49
15 78 101 43
62 98 114 108
"""
