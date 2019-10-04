q=int(input()) #ilk input kac veri girilecegi.
sayac=[] #verilerin atilacagi sayac

for l in range(q): #kac veri girilecekse o kadar donecek bir dongu kuruyorum.
    sayi=[] #her bir verinin sayisinin atilacagi bir liste olusturuyorum. 
    aralik=list(map(int,input().split())) #veri araligi aliyorum.Bu araligi
    a=aralik[0] #kullanabilecegim bir hale getiriyorum. 
    b=aralik[1]
    
    for t in range(a,b+1): #araliktaki sayilarin uzerinde dolaniyorum.
        k=t**0.5 #bu sayilarin karekoklerini aliyorum
        if k.is_integer()==True: #bu karekok tamsayi ise bu sayiyi bir listeye 
            sayi.append(k)#ekliyorum. 

    sayac.append(len(sayi))#Ardindan bu listenin uzunlugunu ayri bir listeye ekliyorum

for e in sayac: #liste uzunluk bilgisi olan sayac verilerini donguyle alt alta yazdiriyorum
    print(e)

#KOD DOGRU CALISIYOR AMA HACKERRANK TE BUYUK VERILER ICIN YAVAS CALISTIGINDAN
#DOLAYI TUM TESTLERI GECEMIYOR. 
        
            
