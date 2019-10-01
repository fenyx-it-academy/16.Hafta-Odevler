n = int(input())
ar = list(map(int, input().rstrip().split()))

lst = [i for i in set(ar) if ar.count(i) % 2 == 1]
print(int((len(ar) - len(lst)) / 2))
