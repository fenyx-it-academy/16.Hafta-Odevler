n = int(input())
ar = list(map(int, input().rstrip().split()))
list2=[]
num=0
for i in set(ar):
    list2.append((ar.count(i)))
for i in list2:
    if i >= 2 and i // 2 >= 1:
        num += (i //2)
print(num)