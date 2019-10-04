def sockMerchant(n, ar):
    count = 0
    list = []
    for i in ar:
        if i not in list:
            list.append(i)

        else:
            count += 1
            list.remove(i)

    print(count)


n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
