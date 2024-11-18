def compareTriplets(a, b):
    # Write your code here
    totalA = 0
    totalB = 0
    for num in range(len(a)):
        if a[num] > b[num]:
            totalA += 1
        elif b[num] > a[num]:
            totalB += 1
    return [totalA, totalB]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
