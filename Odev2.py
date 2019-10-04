# Soru:
# İngilizce karakterlerden oluşan bir string var elimizde.
# Bu stringe iki işlem uygulayabiliyoruz.
# 1. Sonuna küçük harf ekleyebiliyoruz
# 2. En sondan bir karakter silebiliyoruz.
# Bu işlemi boş stringe uygulayınca boş bir string veriyor.
# Bize bir k sayısı integer olarak veriliyor, iki de string, s ve t.
# s stringine k sayısı kadar yukarıdaki iki işlem (append, delete)
# uygulayarak t stringine dönüştürebilir miyiz tesbit etmemiz lazım.
# Oluyorsa Yes, olmuyorsa No yazdırmamız lazım.
# Örnekte s=[a,b,c], t=[d,e,f], k=6
# Önce s’nin tüm elemanlarını 3 hamlede siliyoruz, sonra t’nin elemanlarını
# 3 hamlede ekliyoruz. Toplam 6 hamlede s’yi t’ye dönüştürmüş oluyoruz.


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    count = 0

    if len(s) > len(t):
        while True:
            s = s[:-1]
            count += 1
            if s == t:
                break
            else:
                continue
    elif(len(t) > len(s)):
        while True:
            s = s[:-1]
            count += 1

            if s == t:
                break
            else:
                continue


    print('count:',count)

s = input()

t = input()

k = int(input())

result = appendAndDelete(s, t, k)
