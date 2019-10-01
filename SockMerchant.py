n=9
ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
def sockMerchant(n, ar):
    br=set(ar)
    count=[]
    for i in br:
        count.append((ar.count(i))//2)
    return(sum(count))