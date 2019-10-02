def appendAndDelete():
    a = input()
    b = input()
    k = int(input())
    for i in range(max(len(a),len(b))):
        if min(len(a),len(b))<i+1:
            break
        elif a[i] != b[i]:
            break
    if (len(a[i:])+len(b[i:])<=k and (k-(len(a[i:])+len(b[i:])))%2==0) or len(a)+len(b)<=k:
        print('Yes')
    else:
        print('No')

appendAndDelete()
