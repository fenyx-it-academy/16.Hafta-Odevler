def squares(a, b):
    count = 0
    for i in range(a, b+1):
        for j in range(0, b+1):
            if j*j == i:
                count += 1
    print(count)

q = int(input("q:"))

for q_itr in range(q):

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])


    result = squares(a, b)


