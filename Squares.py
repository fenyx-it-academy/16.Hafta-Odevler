import math


# code below is my initial thought. (Lines 8-13)
# It works fine, however, with huge number of tests it fails due to the time limit.
# The second code (lines 7-8) has a much simpler but accurate logic. Thus it passes all test cases.
'''
def squares(a, b):
    count = 0
    for i in range(a, b+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            count += 1
    print(len(int_squares))
'''


def squares(a, b):
    print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a))+1)


q = int(input())

for q_itr in range(q):
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    squares(a, b)
