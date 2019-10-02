print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


q = int(input())
for q_itr in range(q):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    print(int(b ** 0.5) - int((a - 1) ** 0.5))
