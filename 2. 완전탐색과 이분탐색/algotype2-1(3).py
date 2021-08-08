def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    d = [a, b, c]
    count = 0
    e = []

    for o in d:
        e.append(count)
        print("o 원점", count)
        count = 0
        for i in range(len(o) - 1):
            print("i 원점", i)
            a1 = len(answers) // len(o)
            a2 = len(answers) % len(o)
            m = 0
            n = 0
            if a1 == 0:
                print("a1 == 0")
                while m < a2:
                    if o[m] == answers[m]:
                        count += 1
                        m += 1
                        print("count1")
                    elif o[m] != answers[m]:
                        m += 1
                        print("con1")
            elif a1 > 0:
                print("a1 > 0")
                while m <= a1 and n < a2:
                    if m < a1:
                        if a[i] == answers[i + m * len(o)]:
                            count += 1
                            m += 1
                            print("count2")
                        elif a[i] != answers[i + m * len(o)]:
                            m += 1
                            print("con2")
                    elif m == a1:
                        if a[n] == answers[n + m * len(o)]:
                            count += 1
                            n += 1
                            print("count3")
                        elif a[n] != answers[n + m * len(o)]:
                            n += 1
                            print("con3")

            #     while m <= a1 and n < a2:
            #         print("m 원점", m, i)
            #         if m < a1:
            #             if o[i] == answers[i+len(o)*m]:
            #                 count += 1
            #                 m += 1
            #                 print("count 1")
            #             elif o[i] != answers[i+len(o)*m]:
            #                 m += 1
            #                 print("con 1")
            #         elif m == a1:
            #             if o[n] == answers[len(o)*m+n]:
            #                 count += 1
            #                 n += 1
            #                 print("count 2")
            #             elif o[n] != answers[len(o)*m+n]:
            #                 n += 1
            #                 print("con 2")
            #
            # elif len(o) > len(answers):
            #     while n < a2:
            #         print("n 원점", n, i)
            #         if o[n] == answers[n]:
            #             count += 1
            #             n += 1
            #         elif o[n] != answers[n]:
            #             n += 1
        print(e)

    answer = []
    return answer


answers = [1, 2, 3, 4, 5, 1]
print(solution(answers))
#################진행중