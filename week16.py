# 1 sherlock and squares

import math
q = int(input())
for q_itr in range(q):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    sqr_a = math.ceil(math.sqrt(int(ab[0])))
    sqr_b = math.ceil(math.sqrt(int(ab[1])))
    count = 0
    for x in range(sqr_a, sqr_b+1):
        if pow(x, 2) <= b:
            count += 1
    print(count)


# 2 Append and Delete


s = input()
t = input()
k = int(input())
aynikarakter=0

for y in range(min([len(s),len(t)])):
    if s[y]==t[y]:
        aynikarakter+=1
    else:
        break

fark = abs(len(s)-aynikarakter) + abs(len(t)-aynikarakter)

if fark <= k and fark%2 == k%2 or len(s) + len(t) < k:
    print("Yes")
else:
    print("No")


#3 Sock Merchant


n = int(input())
ar = list(map(int, input().rstrip().split()))
tek=set(ar)
liste=[]
for i in set(ar):
    liste.append(ar.count(i)//2)
print(sum(liste))
