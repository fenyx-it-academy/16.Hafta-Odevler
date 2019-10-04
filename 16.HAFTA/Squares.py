# Complete the squares function below.
def squares(a, b):
    a = [3,9]
    b = [17,24]

    counta = []
    countb = []
    for i in range(a[0], a[1] + 1):
        if int((i ** 0.5)) ** 2 == int(i):
            counta.append(i)
    for i in range(b[0], b[1] + 1):
        if int((i ** 0.5)) ** 2 == int(i):
            countb.append(i)

    return len(counta), len(countb)


file = open("py.txt","w")
result = squares("a", "b")

file.write(str(result) + '\n')

file.close()

