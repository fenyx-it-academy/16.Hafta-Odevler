def appendAndDelete(s, t, k):
    slist = []
    tlist = []
    if len(s)+len(t)<=k:
        print('YES')
    for i in s:
        slist.append(i)
    for i in t:
        tlist.append(i)
    x = min(len(slist), len(tlist))
    y = max(len(slist), len(tlist))
    count = 0
    c_count=0
    if len(slist)>=len(tlist):
        for i in range(x):
            while slist[i] == tlist[i]:
                count += 1
                break
            else:
                break
        if (y - count) + (x - count) <= k:
            print("Yes")
        else:
            print("No")
    else:
        for i in range(x):
            while slist[i] == tlist[i]:
                c_count += 1
                break
        if y-c_count*2<=k:
            print("Yes")
        else:
            print("No")

appendAndDelete('abcd','abcdert',10)