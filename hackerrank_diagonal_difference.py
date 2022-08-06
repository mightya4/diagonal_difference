#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    length_of_array = len(arr)
    first_diagonal_sum = 0
    second_diagonal_sum = 0
    index = 0
    #Calculate sum of first diagonal
    for i in range(0, length_of_array):
        j = i
        first_diagonal_sum += arr[i][j]
    j = 0
    #Calculate sum of second diagonal
    for i in range(length_of_array - 1, -1, -1):
        second_diagonal_sum += arr[i][j]
        j += 1
            

    return  abs(first_diagonal_sum - second_diagonal_sum)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
