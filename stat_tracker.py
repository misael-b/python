#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    maxScore = scores[0]
    minScore = scores[0]
    maxCounter = 0
    minCounter = 0
    for i in range(1, len(scores)):
        if scores[i]>maxScore:
            maxCounter+=1
            maxScore = scores[i]
        if scores[i]<minScore:
            minCounter+=1
            minScore = scores[i]
    return [maxCounter, minCounter]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

