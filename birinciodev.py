
q = int(input())
for q_itr in range(q):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    nummer=int(b**(1/2))-int((a-1)**(1/2))
    print(nummer)