
a=[10 ,20 ,20, 10 ,10 ,30, 50, 10 ,20]
kutu=[]
w=[]
for i in a:
    if i not in kutu:
        x=a.count(i)
        kutu+=[i]
        w+=[x//2]
print(sum(w))
