def sockMerchant(n, ar):
    yeni_arr=list(set(ar))
    sayac=0
    count=0
    a=0
    while sayac<len(yeni_arr):
        count+=(ar.count(yeni_arr[a])//2)
        a+=1
        sayac+=1
    return count
n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)