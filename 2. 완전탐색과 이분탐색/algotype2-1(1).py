def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1 = 0
    b1 = 0
    c1 = 0
    ans = list(answers)
    m = 0
    n = 0
    a2 = len(answers) // len(a)
    a3 = len(answers) % len(a)
    print(a2, a3)
    for i in range(len(a)):
        print("원점")
        while m <= a2:
            if m == a2:
                if a3 != 0:
                    while n <= a3 and a3 > 0:
                        if n == a3:
                            print(a1,n,"end2")
                            n=0
                            m=0
                            break
                        elif n < a3:
                            print("a++")
                            n += 1
                            a1 += 1
                elif a3 == 0:
                    if ans[(i+1)*m] == a[i]:
                        print("a+2")
                        print(m,i,a1,a2,a3)
                        a1 += 1
                        m = 0
                        break
            elif m <= a2:
                if ans[m*(i+1)] == a[i] and i!=0:
                    print("a+3")
                    print(m, i, a1, a2, a3)
                    a1 += 1
                    m += 1
                    continue
                elif ans[m*(i+1)] == a[i] and i == 0:
                    print("i==0")
                    print(m, i, a1, a2, a3)
                    m+=1

            # elif ans[i] == a[i]:
            #     print("a+")
            #     a1 += 1
            #     m += 1
            else:
                print("dead")
                break
        print(a1)

    # for i in range(len(answers)):
    #     print("원점2")
    #     while m < len(b):
    #         if m == len(b):
    #             print("b-")
    #             m = 0
    #             break
    #         elif ans[i] == b[i]:
    #             b1 += 1
    #             print("b+")
    #             continue
    #
    # for i in range(len(answers)):
    #     print("원점3")
    #     while m < len(c):
    #         if m == len(c):
    #             print("c-")
    #             m = 0
    #             break
    #         elif ans[i] == c[i]:
    #             c1 += 1
    #             print("c+")
    #             continue

    answer = answer.sort()
    return answer
ba = [1,2,3,4,1,2,3,4,5,1]
print(solution(ba))
## 1차시 2시간 실패