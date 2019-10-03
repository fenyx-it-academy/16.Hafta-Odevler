## Python'daki ceil () yöntemi, x'in tavan değerini döndürür,
##yani x'den küçük olmayan en küçük tam sayı.


## Python'daki floor () yöntemi, x'in tabanını,
##yani x'ten büyük olmayan en büyük tam sayıyı döndürür.

from math import *
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    print (int(b - a) + 1)
