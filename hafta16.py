"""Squares"""

import math
#math.ceil yukari yuvarliyor
#math.floor asagi yuvarliyor(+1 halini asagi yuvarladim.b tamkare ise dahil olmasi icin
def square(a,b):
    lst=[x for x in range(math.ceil(a**(1/2)),math.floor(b**(1/2)+1))]
    return len(lst)

q = int(input())

ab = [input().split() for i in range(q)]
for i in range(q):
    a=int(ab[i][0])
    b=int(ab[i][1])
    print(square(a,b))
#############################################

"""Sock Merchant"""

n = int(input())
ar = list(map(int, input().rstrip().split()))
set_ar=set(ar)
sock_pair=0
for i in set_ar:
    sock_pair+=(ar.count(i)//2)
print(sock_pair)

##############################################
"""append and delete"""

s = input()
t = input()
k = int(input())
counter=0
i=0
while i<min(len(s),len(t)):     #ikisinde de bastan itibaren ayni olan kisim uzunlugunu bulalim
    if s[i]==t[i]:
        i+=1
    else:
        break
counter+=(len(s)-i)+(len(t)-i)  #iki listenin ayni olan kisimlarindan sonraki silinip yeniden yazilacak kisim sayisi
if counter>k:
    print("No")     #eger benzemeyen kisim hamle sayisindan fazla ise donusum gerceklesemez
elif k>len(s)+len(t):
    print("Yes")    #tamamen silip tekrar yazacak kadar ya da daha fazla hamle sayisi varsa donusum gerceklesir
elif (counter-k)%2==0:
    print("Yes")    #degisecek harflerin sayisi hamle yapip kalan kisim fazladan 1del 1 append yapariz.+2 hamle demek
                    #fark ikiye tam bolunmeli
else:
    print("No")