def fonnk(a,b):
    sonuc=0
    for i in range(1,40000):
        c=i**2
        if c> b:
            break
        else:
            if c >=a:
                sonuc+=1
    return sonuc
    
    
print(fonnk(1,50))




        
