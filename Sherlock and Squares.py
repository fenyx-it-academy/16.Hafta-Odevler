# Complete the squares function below.
def squares(a, b):
    result = []
    for i in range(b):
        if i**2 in range(a, b + 1):
            result.append(i)
        elif i**2>=b:
            break
    if len(result)<=0:
        return(0)
    else:
        return(len(result))
squares(17,24)