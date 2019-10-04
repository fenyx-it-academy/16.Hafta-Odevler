def sockMerchant(n, ar):
    arset=set(ar)
    cift=0
    for i in arset:
        cift+=(ar.count(i)//2)
    print(cift)
n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
