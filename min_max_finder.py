#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    maxSum = 0
    minSum = 0
    for i in range(len(arr)):
        if i == 0:
            minSum += arr[i]
        elif i == len(arr)-1:
            maxSum += arr[i]
        else:
            minSum += arr[i]
            maxSum += arr[i]
    print(str(minSum) + " " + str(maxSum))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

