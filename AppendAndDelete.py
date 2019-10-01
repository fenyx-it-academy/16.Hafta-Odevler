def appendAndDelete(s, t, k):
    same = 0
    for i in range(min(len(s), len(t))):     # Finding how many letters from the start are the same, if any.
        if s[i] == t[i]:
            same += 1
        else:
            break
    append_for_sure = len(t) - same
    delete_for_sure = len(s) - same
    if append_for_sure + delete_for_sure > k:
        print('No')
    else:
        if same == len(s):
            if k - append_for_sure - same*2 > 0:
                print('Yes')
            elif (k - append_for_sure) % 2 == 0:
                print('Yes')
            else:
                print('No')

        else:
            if (k - append_for_sure - delete_for_sure) == 0:
                print('Yes')
            elif (k - append_for_sure - delete_for_sure - same) < 0:
                if (k - append_for_sure - delete_for_sure) % 2 == 0:
                    print('Yes')
                else:
                    print('No')
            else:
                if (k - append_for_sure - delete_for_sure - same) >= 0:
                    print('Yes')
                else:
                    print('No')


s = input()

t = input()

k = int(input())


appendAndDelete(s, t, k)

