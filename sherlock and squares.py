def squares(a, b):
    sayi=int(b**(0.5))-int((a-1)**(0.5))
    print(sayi)
q = int(input())
for q_itr in range(q):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    result = squares(a, b)
