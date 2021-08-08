def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = list(answers)
    a1 = len(answers) // len(a)
    a2 = len(answers) % len(a)
    b1 = len(answers) // len(b)
    b2 = len(answers) % len(b)
    c1 = len(answers) // len(c)
    c2 = len(answers) % len(c)
    aa=0
    bb=0
    cc=0

    for i in range(len(a)):
        m = 0
        n = 0
        print(a1,a2,i,"a")
        if a2 == 0:
            while m <= a1 - 1:
                if m == 0:
                    if ans[len(a)*m+i] == a[i]:
                        aa += 1
                        m += 1
                    elif ans[len(a)*m+i] != a[i]:
                        m += 1

                elif m != 0:
                    if ans[len(a)*m+i] == a[i]:
                        aa += 1
                        m += 1
                    elif ans[len(a)*m+i] != a[i]:
                        m += 1

        elif a2 != 0:
            while m <= a1:
                if len(a)*m+i >= len(answers):
                    print ("dead")
                    break
                elif m == a1:
                    print(len(a) * m + i, i, "m==a1-1")
                    while n < a2 and i < a2:
                        if ans[len(a)*m+i] != a[n]:
                            n += 1
                        elif ans[len(a)*m+i] == a[n]:
                            aa += 1
                            n += 1
                            print(len(a)*m+i, n)
                            print("a+3")

                if m == 0:
                    print(len(a) * m + i, i, "m==0")
                    if ans[len(a)*m+i] != a[i]:
                        m += 1
                    elif ans[len(a)*m+i] == a[i]:
                        aa += 1
                        m += 1
                        print("a+4")

                elif m != 0:
                    print(len(a) * m + i, i, "m!=0")
                    if ans[len(a) * m + i] == a[i]:
                        aa += 1
                        m += 1
                        print(len(a) * m + i, i, "a+5")
                    elif ans[len(a) * m + i] != a[i]:
                        m += 1
                        print(len(a) * m + i, i, "a-5")
    #
    # for i in range(len(b)):
    #     m = 0
    #     n = 0
    #     print(b1,b2,"b")
    #     if b2 == 0:
    #         while m <= b1 - 1:
    #             if m == 0:
    #                 if ans[len(b) * m + i] == b[i]:
    #                     bb += 1
    #                     m += 1
    #                 elif ans[len(b) * m + i] != b[i]:
    #                     m += 1
    #
    #             elif m != 0:
    #                 if ans[len(b) * m + i] == b[i]:
    #                     bb += 1
    #                     m += 1
    #                 elif ans[len(b) * m + i] != b[i]:
    #                     m += 1
    #
    #     elif b2 != 0:
    #         while m <= b1-1:
    #             if len(b)*m+i >= len(answers):
    #                 print("dead")
    #                 break
    #             elif m == b1:
    #                 print(m, n, i, bb, 11)
    #                 while n < b2 and i < b2:
    #                     if ans[len(b) * m + i] != b[n]:
    #                         n += 1
    #                         print(m,n,i,bb)
    #                     elif ans[len(b) * m + i] == b[n]:
    #                         bb += 1
    #                         n += 1
    #                         print(m,n,i,bb)
    #                         print("b+3")
    #
    #
    #             if m == 0:
    #                 print(m, n, i, bb,22)
    #                 if ans[len(b) * m + i] != b[i]:
    #                     m += 1
    #                 elif ans[len(b) * m + i] == b[i]:
    #                     bb += 1
    #                     m += 1
    #                     print("b+4")
    #
    #             elif m != 0:
    #                 print(m, n, i, bb,33)
    #                 print(len(b) * m + i)
    #                 if ans[len(b) * m + i] == b[i]:
    #                     bb += 1
    #                     m += 1
    #                     print("b+5")
    #                 elif ans[len(b) * m + i] != b[i]:
    #                     m += 1
    #
    # for i in range(len(c)):
    #     m = 0
    #     n = 0
    #     print(c1,c2,"c")
    #     if c2 == 0:
    #         while m <= c1 - 1:
    #             if m == 0:
    #                 if ans[i] == c[i]:
    #                     bb += 1
    #                     m += 1
    #                 elif ans[i] != c[i]:
    #                     m += 1
    #
    #             elif m != 0:
    #                 if ans[len(c) * m + i] == c[i]:
    #                     bb += 1
    #                     m += 1
    #                 elif ans[len(c) * m + i] != c[i]:
    #                     m += 1
    #
    #     elif c2 != 0:
    #         while m <= c1 - 1:
    #             if len(c) * m + i >= len(answers):
    #                 print("dead")
    #                 break
    #             elif m == c1:
    #                 print(m, n, i, cc, 11)
    #                 while n < c2 and i < c2:
    #                     if ans[len(c) * m + i] != c[n]:
    #                         n += 1
    #                         print(m, n, i, cc)
    #                     elif ans[len(c) * m + i] == c[n]:
    #                         cc += 1
    #                         n += 1
    #                         print(m, n, i, cc)
    #                         print("c+3")
    #
    #             if m == 0:
    #                 print(m, n, i, cc, 22)
    #                 if ans[len(c) * m + i] != c[i]:
    #                     m += 1
    #                 elif ans[len(c) * m + i] == c[i]:
    #                     cc += 1
    #                     m += 1
    #                     print("c+4")
    #
    #             elif m != 0:
    #                 print(m, n, i, cc, 33)
    #                 print(len(c) * m + i)
    #                 if ans[len(c) * m + i] == c[i]:
    #                     cc += 1
    #                     m += 1
    #                     print("c+5")
    #                 elif ans[len(c) * m + i] != c[i]:
    #                     m += 1

    answerb= [aa,bb,cc]
    print(answerb)
    answer = []
    return answer

answers = [2,2,2,2,2,2,2]

print(solution(answers))