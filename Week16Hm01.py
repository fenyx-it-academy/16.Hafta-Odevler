q = int(input())
for q_itr in range(q):
    a, b = input().strip().split(' ')
    a = int(a)
    b = int(b)
    num = 0
    for i in range(a,b+1):
        if (i** 0.5) % 2 == 0 or (i** 0.5) % 2 == 1:
            num += 1
    print(num)



