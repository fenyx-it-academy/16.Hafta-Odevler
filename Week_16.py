# Hw.-1.---------------------------------------------------------------------------------
t = int(input())
for t_itr in range(t):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    nummer=int(b**(1/2))-int((a-1)**(1/2))
    print(nummer)


# Hw.-2.---------------------------------------------------------------------------------

def app_del(s, t, k):
    list_s=[ i for i in s]
    list_t=[ i for i in t]
    x=len(list_s)
    y=len(list_t)
    ortak=[]
    for i in range(max(x,y)+1):
        if list_s[:i] == list_t[:i]:
            ortak.append(list_s[:i])
    z=len(comm[-1])
    if ((x+y)-2*z)>k:
        print("No")
    elif ((x+y)-2*z)%2==k%2:
        print("Yes")
    elif k>(x+y):
        print("Yes")
    else:
        print("No")

s = input()
t = input()
k = int(input())
app_del(s, t, k)



# Hw.-3.---------------------------------------------------------------------------------

def sockMerchant(n, ar):
    new_arr=list(set(ar))
    say=0
    count=0
    a=0
    while say<len(new_arr):
        count+=(ar.count(new_arr[a])//2)
        a+=1
        say+=1
    return count
n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)