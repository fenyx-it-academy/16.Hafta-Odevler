def fonnk (s,t,k):
    slen=len(s)
    tlen=len(t)
    aynı=0
    for i in range (1,slen+1):
        if s[0:i]==t[0:i]:
            aynı+=1
    k1=slen-aynı
    k2=tlen-aynı
    if k1+k2 >k:
        return "No"
    if k==k1+k2:
        return "Yes"
    if k1+k2<k:
        if (2*aynı)+k1+k2<k:
            return "Yes" 
        if (k-(k1+k2))%2==0:
            return "Yes"
        else:
            return "No"

print(fonnk("abcd","abcdert",10))







      
