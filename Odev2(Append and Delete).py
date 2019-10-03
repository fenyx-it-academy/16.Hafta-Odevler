def appendAndDelete(s, t, k):
    liste_s=[ i for i in s]                 # string listeye cevrildi.
    liste_t=[ i for i in t]
    x=len(liste_s)
    y=len(liste_t)
    ortak=[]
    for i in range(max(x,y)+1):             # bu donguyle bastan itibaren ortak olan harfler depolandi.
        if liste_s[:i] == liste_t[:i]:
            ortak.append(liste_s[:i])
    z=len(ortak[-1])                        # ortak harflerin uzunlugu alindi.
    if ((x+y)-2*z)>k:                       # burda ortak harfler disinda kalan toplam harf sayisi k dan buyukse
        print("No")                         # degisim olamayacindan no bastirildi.
    elif ((x+y)-2*z)%2==k%2:                # ortak olmayan harflerin tek mi cift mi oldugu sorgulandi. eyer k ve bu sayi
        print("Yes")                        # (tek,tek) veya (cift,cift) olmasi durumunda yes bastirildi.
    elif k>(x+y):                           # k (x,y) toplamindan buyukse her turlu yes oldu.
        print("Yes")
    else:                                   # diger tum durumlarda no oldu.
        print("No")

s = input()
t = input()
k = int(input())
appendAndDelete(s, t, k)