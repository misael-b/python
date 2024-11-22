#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    totalPositive = 0
    totalNegative = 0
    totalZero = 0
    for num in arr:
        if num < 0:
            totalNegative += 1
        elif num > 0:
            totalPositive+=1
        else:
            totalZero += 1
    print(totalPositive/len(arr))
    print(totalNegative/len(arr))
    print(totalZero/len(arr))
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

