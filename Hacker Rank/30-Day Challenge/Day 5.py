#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lights' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

def lights(n):
    # Write your code here
    return (pow(2, n, 100000) - 1) % 100000

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
