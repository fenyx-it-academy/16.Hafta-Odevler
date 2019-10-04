def fonnk(s,k):
    renk={}     #her renk kodundan kaç tane olduğunu belirten bir sözlük
    sonuc=0
    for i in s: 
        if i in renk: 
            renk[i]=1+renk[i]
        else:
            renk[i]=1
    print(renk)
    for k in renk:
        sonuc+=renk[k]//2
    return sonuc


print(fonnk([2,2,2,4,6,6,6,6,7,7],10))
      
            
    
