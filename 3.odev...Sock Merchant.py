
def sockMerchant():
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    x = [ar.count(i) // 2 for i in set(ar) if 1 <= ar.count(i) // 2]
    print(sum(x))
sockMerchant()