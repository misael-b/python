#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ans = 0
    colors = {}
    if n == 1:
        return 0
    for color in ar:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] = colors[color] + 1
    
    for num in list(colors.values()):
        if num % 2 == 0:
            ans += num /2
        else:
            ans += (num - 1)/2
    return int(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

