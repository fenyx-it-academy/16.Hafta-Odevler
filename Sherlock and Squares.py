q = int(input())
for q_itr in range(q):
    a, b = list(map(int,input().split()))
    lst = [i for i in range(a, b + 1) if (i ** 0.5).is_integer()]
    print(len(lst))
