print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

                                                        # Bu soruya alternatif cozum Counter ile cok basit yapiliyormus. Saydiriyorsun aynilari sonra 2tane olanlari boluyorsa ekliyorsun!
def sockMerchant(n, ar):
    set_of_ar = set(ar)                                 # bize verilen sayilarin kumesini alinca elemanlari teke indirmis oluyor
    similar_pair = []                                   # benzer ciftleri bu kumeye ekleyelim
    for i in set_of_ar:                                 # kumemizi tariyoruz
        similar_pair.append(ar.count(i)//2)             # ar icinde benzer olanlari 2 ye bolup tam bolunmusleri saydiriyoruz ve bos listeye ekliyoruz
    return print(sum(similar_pair))                     # listede olanlarin toplami bize sonucu veriyor


n = int(input())
ar = list(map(int, input().split()))

sockMerchant(n, ar)

