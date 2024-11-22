#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    timeArray = s.split(":")
    if timeArray[-1][-2:] == "PM" and timeArray[0] == "12":
        return s[0:-2]
    elif timeArray[-1][-2:] == "PM":
        hour = int(timeArray[0])
        hour = 12 +hour
        return str(hour) + ":" + timeArray[1] + ":" +timeArray[-1][:-2]
    elif timeArray[0] == "12":
        return "00" + ":" + timeArray[1] + ":" +timeArray[-1][:-2]
    else:
        return s[0:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

