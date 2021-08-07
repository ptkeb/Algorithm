class aa:
    def solution(progresses, speeds):
        days = []
        answer = []
        a1 = progresses
        b1 = speeds
        print(a1)
        for i in range(len(a1)):
            m = 1
            while m <= 101:
                if a1[i] + m * (b1[i]) <= 100:
                    m += 1
                    continue
                else:
                    m-=1
                    days.append(m)
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


## queue를 이용한 작업
# 정확도 90.9, 구성요소 1개짜리를 위한 코드가 필요할듯