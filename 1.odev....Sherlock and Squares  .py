def squares():
    t = []
    q = int(input())
    for i in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])
        x = []
        for i in range(a, b + 1):
            for j in range(i + 1):
                if j ** 2 == i:
                    x.append(i)
                    break
        t.append(len(x))
    for i in t:
        print(i)
squares()