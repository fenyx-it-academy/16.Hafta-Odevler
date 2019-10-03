def appendAndDelete(s, t, k):
    liste_s=[ i for i in s]
    liste_t=[ i for i in t]
    x=len(liste_s)
    y=len(liste_t)
    ortak=[]
    for i in range(max(x,y)+1):
        if liste_s[:i] == liste_t[:i]:
            ortak.append(liste_s[:i])
    z=len(ortak[-1])
    if ((x+y)-2*z)>k:
        print("No")
    elif ((x+y)-2*z)%2==k%2:
        print("Yes")
    elif k>(x+y):
        print("Yes")
    else:
        print("No")

s = input()
t = input()
k = int(input())
appendAndDelete(s, t, k)
