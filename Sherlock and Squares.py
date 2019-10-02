def squares():
    q = int(input())
    for q_itr in range(q):
        ab = input().split()
        a = (int(ab[0])-1)**.5
        b = int(ab[1])**.5
        print(int(b)-int(a))
result = squares()

