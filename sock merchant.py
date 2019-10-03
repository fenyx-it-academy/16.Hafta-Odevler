n = int(input())
ar = list(map(int, input().rstrip().split()))
tek=set(ar)
liste=[]
for i in set(ar):
    liste.append(ar.count(i)//2)
print(sum(liste))