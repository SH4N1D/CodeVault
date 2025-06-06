#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#

def beautifulPairs(A, B):
    freqA = Counter(A)
    freqB = Counter(B)

    matches = 0

    for val in freqA:
        if val in freqB:
            matches += min(freqA[val], freqB[val])
    
    if matches == len(A):
        return matches - 1
    else:
        return matches + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
