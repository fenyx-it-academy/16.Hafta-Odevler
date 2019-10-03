###################SCHERLOCK'S MATH

def squares():
    q = int(input())   #burada birden fazla line icin nasil input alacagim
    for q_itr in range(q):
        ab = list(map(int, input().split()))    #araligin basi a, sonu b olmali so b+1 yapiyoruz asagida
        a = ab[0]
        b = ab[1]
        mylist = [i for i in range(b+1) for j in range(a, (b+1)) if i ** 2 == j]
        print(len(mylist))

squares()

#Dogru ve calisiyor ama time limitini asiyormus

#Kimkimin karesi degil de kim kimin karekokunden gittim basta,
#ama o durumda sonucun integer olup olmayacagini kontrol edecek bir fonks bilmiyorum
#cunku sonuc hep float olacak bunu isinteger ile kontrol edemem, int'e cevirsem zaten 4.0
# olsa da 4 olacak 4.5 olsa da, bu yuzden bu daha mantikli

#########################APPENDDELETE
def appendAndDelete(s, t, k):
    s = input()   #to be deleted
    t = input()    #to be replaced
    k = int(input())  #move limit

    if k >= (len(t)+len(s)):  # empty list deletions is possible
        print('Yes')

    # to find common lenght of elements in them
    commons = 0
    for i in range(0, min(len(s), len(t)), 1):
        if s[i] == t[i]:
            commons += 1
        else:
            break
    if ((k - len(s) - len(t) + 2 * commons) % 2 == 0):
        print('Yes')

    else:
        print('No')


appendAndDelete('ayse', 'fatma', 5)

#idle'de yes ve no veriyor hackerrankte de error veriyor, no olayini cozemiyom cozecem ins 

##################SOCK MERCHANT
def sockMerchant():
    n = input() #numb of socks in th epile
    ar = list(map(int, input().split())) #colors of each sock
                 #n space seperated integers describing colors of socks
    remainders=[i for i in set(ar) if ar.count(i)%2 ==1] #her elemani br kere count edelim diye
                    #ar setindeki her bir elemani ar listesinde say demek istiyorum
    print(int((len(ar)-len(remainders))/2))
sockMerchant()   #print the pairs of socks

#Bu sekilde calisiyor ama parametreyi parantezin icine koyunca olmuyor

#Hello tehre, normalde fonksiyona istendigi gibi n ve ar'i da veriyorum ama neden oldugunu bilmiyorum hata veriyor hep,
#asagiya parametre girince de super sacma oluyor o da hata veriyor.
























