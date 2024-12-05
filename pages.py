#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p == 1 or p == n or (n % 2 != 0 and p==n-1):
        return 0
    halfway = int(n / 2)
    if p <= halfway:
        return int((p / 2))
    else:
        if p % 2 == 0:
            return int((n-p)/2)
        else:
            return int((n-p+1)/2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

