q = int(input())
for q_itr in range(q):
    a, b = list(map(int, input().split()))
    result = int(b ** (1 / 2)) - int((a - 1) ** (1 / 2))
    print(result)
