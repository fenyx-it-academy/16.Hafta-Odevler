def appendAndDelete(s, t, k):
    sayi = 0
    while True:
        try:
            if s[sayi] == t[sayi]:
                sayi += 1
            else:
                break
        except:
            break
    if len(s[sayi:]) + len(t[sayi:]) == 0:
        return 'Yes'
    elif len(s[sayi:]) + len(t[sayi:]) <= k:
        if k % 2 == (len(s[sayi:]) + len(t[sayi:])) % 2:
            return 'Yes'
        elif k % 2 != 0 and (len(s[sayi:]) + len(t[sayi:])) % 2 == 0:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'
s = input()
t = input()
k = int(input())
print(appendAndDelete(s, t, k))