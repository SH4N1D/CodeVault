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
    fsum=0
    ssum=0
    for i in range (0,n):
        for j in range (0,n):
            if i==j:
                fsum=fsum+arr[i][j]
    for i in range (0,n):
        for j in range (0,n):
            if j==(n-i-1):
                ssum=ssum+arr[i][j]
    fanswer=abs(fsum-ssum)
    return fanswer

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
