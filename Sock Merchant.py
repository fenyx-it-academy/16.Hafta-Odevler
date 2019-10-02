def sockMerchant():
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    counter=0
    for i in set(ar):
        counter+=ar.count(i)//2
    print (counter)
sockMerchant()