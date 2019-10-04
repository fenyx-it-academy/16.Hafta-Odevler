n=int(input())

ar=list(map(int,input().split()))

counter=0

for i in ar: #liste ustunde dolaniyorum
    if ar.count(i)%2==0: #eger ki cift sayida degerler varsa onlarin direk 
        counter+=ar.count(i)/2 #yarisini alarak sayac ekliyorum
        for l in range(ar.count(i)): #liste ustunde dolanirken ayni islemi
            ar.remove(i) #tekrar etmemek icin inceledigim veriyi siliyorum.
    elif ar.count(i)%2!=0 and ar.count(i)>2: #ayni islemi tek sayida olan
        counter+=(ar.count(i)-1)/2 #veriler icin yapiyorum
        for l in range(ar.count(i)):
            ar.remove(i)
print(int(counter))        
    


    

