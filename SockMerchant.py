def sockMerchant(n, ar):
    no_of_pairs = 0
    global i
    i = 0
    while i < len(ar):
        for k in range(i+1, len(ar)):
            if ar[i] == ar[k]:
                no_of_pairs += 1
                ar.pop(i)
                ar.pop(k-1)
                i = 0
                break
        else:
            i += 1
    print(no_of_pairs)

n = int(input())

ar = list(map(int, input().rstrip().split()))

sockMerchant(n, ar)

