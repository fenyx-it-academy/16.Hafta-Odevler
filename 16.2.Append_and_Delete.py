print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def appendAndDelete(s, t, k):
    count = 0
    length_s = len(s)                                                   # girilen ve istenen stringlerin len ini alalim
    length_t = len(t)                                                   # simdi kac eleman birbirine benziyor ve adetlerini sayalim
    for i in range(min([length_s, length_t])):                          # iki len arasinda hangisi kisa ise range miz oraya kadar donsun.
        if s[i] == t[i]:                                                # istenen verilenlerin bulundugu indexlerdeki elemanlar esit olup olmadigini check etsin
            count += 1
        else:                                                           # farkli ise donguden ciksin
            break

    between_difference = abs(length_s - count) + abs(length_t - count)      # eger yukardaki donguden ayni eleman varsa uzunluklardan cikar ve ikisini toplayinca bize sonucta kac elemanla yapacagimizi ver

    if between_difference <= k and between_difference % 2 == k % 2 or length_s + length_t < k:     # and li kisim benzer harfler ciktiginda yapilmasi gereken ve or sonrasi hic benzer olmayinca
        print("Yes")
    else:
        print("No")


s = input()
t = input()
k = int(input())
appendAndDelete(s, t, k)
