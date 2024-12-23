#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    if "a" not in s:
        return 0
    num = n // len(s)
    remainder = n % len(s)
    occurances = 0
    for i in range(len(s)):
        if s[i] == "a":
            occurances += 1
            
    ans = occurances * num
    for i in range(remainder):
        if s[i] == "a":
            ans += 1
    return ans
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
