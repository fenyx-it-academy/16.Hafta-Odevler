def sockMerchant(n, ar):
    pair={}
    c=0
    for i in ar:
        pair[i]=[ar.count(i),ar.count(i)//2]
    for o in pair.values():
        c+=o[1]
    return c
n = 9
ar = [10,20,20,10,10,30,50,10,20]
result = sockMerchant(n, ar)
print(result)