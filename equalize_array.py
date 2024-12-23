#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    distinctNum = set(arr)
    numbersOfOccurances = []
    for num in distinctNum:
        occurances = arr.count(num)
        numbersOfOccurances.append(occurances)
    numbersOfOccurances.sort()
    return sum(numbersOfOccurances[:-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

