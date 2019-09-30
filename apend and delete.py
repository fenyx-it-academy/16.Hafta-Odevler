s='zzzzz'
t='zzzzzzz'
k=4
# BOYLE SACMA BIR SORU GORMEDIM
z=len(s)
m=len(t)
sayac=0
if z<=m:
    for i in range(z):
        if s[i]==t[i]:
            sayac+=1
        else:
            break
else:
    for i in range(m):
        if s[i]==t[i]:
            sayac+=1
        else:
            break
if z>=m:
    toplam=z-sayac+m-sayac
elif s.count(s[0])+t.count(t[0])==m+z:
    toplam=abs(m-z)
else:
    toplam = z + m

if toplam<=k :
    print('Yes')
else:
    print('No')


