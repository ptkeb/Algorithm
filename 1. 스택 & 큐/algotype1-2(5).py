class aa:
    def solution(progresses, speeds):
        days = []
        answer = []
        a1 = progresses
        b1 = speeds
        print(a1)
        for i in range(len(a1)):
            m = 0
            while m <= 101:
                if a1[i] + m * (b1[i]) <= 100:
                        m += 1
                        continue
                else:
                    if (100 - a1[i]) % b1[i] == 0:
                        m -= 1
                        days.append(m)
                        print("aa")
                        break
                    else:
                        days.append(m)
                        print("bb")
                        break
        print(days)
        if len(days) != 1:
            i = 0
            c = int(days.pop(0))
            d = int(days.pop(0))
            print(c,d)
            count = 0
            while i <= len(days):
                if len(days) == 0:
                    if c >= d:
                        count += 2
                        answer.append(count)
                        break
                    else:
                        count += 1
                        answer.append(count)
                        count = 1
                        answer.append(count)
                        break
                elif c < d :
                    count += 1
                    answer.append(count)
                    c = d
                    d = days.pop(0)

                    print("a",c, d)
                    count = 0
                    continue

                elif c >= d:
                    count += 1
                    d = days.pop(0)
                    print("b",c, d)
                    continue

                else:
                    print("c")
                    break
        else:
            answer.append(days[0])

        return answer


a = [95]
b = [2]
print(aa.solution(a, b))


# 통과 , 문제점은 days를 구할때, 요소가 1개라면 나머지가 0이 아닌것을 추가할때 제대로 추가되지 않은것