#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    gradesArray = []
    for grade in grades:
        if grade < 38:
            gradesArray.append(grade)
        else:
            roundedNum = (grade//5) +1
            roundedScore = roundedNum * 5
            if (roundedScore - grade) < 3:
                gradesArray.append(roundedScore)
            else:
                gradesArray.append(grade)
    return gradesArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

