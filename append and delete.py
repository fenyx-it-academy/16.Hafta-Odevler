s = input()
t = input() 
k = int(input())

for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        result = (len(s) - i) + (len(t) - i)
        break
    else:
        result = abs(len(s) - len(t))
       
if len(s) == len(t):
    result = len(s) + len(t)

if s == t and k <= result:
    print("Yes")

elif k >= result:
    if len(s) < len(t):
        if (k - result) % 2 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")

else:
    print("No")
