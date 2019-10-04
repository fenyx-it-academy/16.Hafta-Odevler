data1=input() #verileri aliyorum
data2=input()
k=int(input())
s=[]
t=[]
count=0
for i in data1: #verileri harf harf liste halinde bos listelere atiyorum
    s.append(i)

for i in data2:
    t.append(i)

for z in range(abs(len(s)-len(t))): #veri sayilarini esitliyorum.ayni anda silme
                                    #islemi yapip tek tek esitligi kontrol edebilmek icin.
    if len(s)>len(t):  # hangi veri buyukse onun fazla harflerini silip sayaca ekliyorum.
        s.pop()
        count+=1
       

    elif len(t)>len(s):
        t.pop()
        count+=1
       
        
    else:    #esitlik saglaninca donguden cikiyorum.
        break

while True:
    if s==t and count<=k: #eger silme islemi sonunda veriler ayniysa ve verilen deger sayacimla
        print("Yes")      #esitse veya buyukse yes basiliyor
        break

    elif s!=t:   #deger ayni degilse her iki listeden de bir harf silinip sayaca ekleniyor
        s.pop()
        t.pop()
        count+=2
        continue

    elif s==t and count>k:  #esitlik saglandiktan sonra sayac veriden buyukse no basiliyor 
        print("No")
        break



    






