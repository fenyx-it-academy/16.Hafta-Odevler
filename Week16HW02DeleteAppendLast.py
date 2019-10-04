s = input()

t = input()

k = int(input())
num=0
if len(s)<=len(t):
    for i in range(len(s)):
        if s[i]==t[i]:
            num+=1
        else:
            break
else:
    for i in range(len(t)):
        if s[i]==t[i]:
            num+=1
        else:
            break
if len(s)>=len(t):
    total= len(s) - num + len(t) - num
elif s.count(s[0]) + t.count(t[0]) == len(s)+len(t) :
    total= abs(len(s) - len(t))
else:
    total = len(s) + len(t)

if total<=k :
    print('Yes')
else:
    print('No')