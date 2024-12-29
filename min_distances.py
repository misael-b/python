#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    ans = len(a)
    setA = set(a)
    if len(setA) == len(a):
        return -1
    for num in setA:
        if a.count(num)>1:
            occurrances = [i for i ,val in enumerate(a) if val==num]
            for i in range(len(occurrances)-1):
                if (occurrances[i+1] - occurrances[i]) < ans:
                    ans = occurrances[i+1] - occurrances[i]
                
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

