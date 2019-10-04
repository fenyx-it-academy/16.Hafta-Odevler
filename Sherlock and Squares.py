q = int(input("eleman sayisi :"))
for q_itr in range(q):
    ab = input("girilecek sayi araligi :").split()
    a=int(ab[0])
    b=int(ab[1])

    if (a**0.5) != int(a**0.5):
         print((int(b**0.5)-(int(a**0.5)+1))+1)
    else:
        print((int(b ** 0.5) - int(a ** 0.5) ) + 1)





