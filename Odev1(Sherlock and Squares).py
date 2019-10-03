import math


def squares(a, b):
    x=math.ceil(a**0.5)         # bu fonksiyon karekoku alinan sayiyi en yakin buyuk tam sayiya yuvarlar
    y=math.floor(b**0.5)        # bu fonksiyon karekoku alinan sayisi en yakin kucuk tam sayiya yuvarlar.
    return (y-x)+1


q = int(input())
for q_itr in range(q):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    result = squares(a, b)
    print(result)