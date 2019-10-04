#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    a = []
    b = []
    for i in ar:
        if i not in a:
            a.append(i)
    for j in a:
        b.append(ar.count(j) // 2)

    return sum(b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant("n", "ar")

    fptr.write(str(result) + '\n')

    fptr.close()
