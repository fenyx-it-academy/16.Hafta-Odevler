import math
def squares(a, b):
    d=0
    for i in range(a,b+1):
        if math.sqrt(i).is_integer()==True:
            print(i,math.sqrt(i))
            d+=1
    return d

print(squares(3 ,9))



