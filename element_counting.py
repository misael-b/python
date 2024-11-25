#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    idsDict = {}
    for bird in arr:
        if bird not in idsDict:
            idsDict[bird] = 1
        else:
            idsDict[bird] = idsDict.get(bird) + 1
    values = list(idsDict.values())
    values.sort()
    maxNum = values[-1]
    ansArray = []
    for number in idsDict.keys():
        if idsDict[number] == maxNum:
            ansArray.append(number)
    ansArray.sort()
    return ansArray[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

