def appendAndDelete(s, t, k):
    count = 0
    for i in range(min(len(s),len(t))):
            if s[i]==t[i]:
                count+=1
            else:
                break;
    if ((len(s) + len(t) - 2 * count) > k):
        return "No"
    elif ((len(s) + len(t) - 2 * count) % 2 == k % 2):
        return  "Yes"
    elif ((len(s) + len(t) - k) < 0):
        return "Yes"
    else:
        return "No"


s = "qwerasdf"
t = "qwerbsdf"
k = 6

result = appendAndDelete(s, t, k)
print(result)



