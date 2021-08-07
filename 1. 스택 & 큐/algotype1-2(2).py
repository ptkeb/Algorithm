class aa:
    def solution(progresses, speeds):
        days = []
        answer = []
        a1 = progresses
        b1 = speeds
        for i in range(len(a1)):
            m = 0
            while m <= 100:
                if a1[i] + m * (b1[i]) <= 100:
                    m += 1
                    continue
                else:
                    m -= 1
                    days.append(m)
                    break
        print(days)

        i = 0
        while i < len(days):
            m = 0
            while m < 100:
                i1 = days[i]

                if i + m +1 == len(days):
                    m += 1
                    i = i + m
                    print(i1, m, "c")
                    answer.append(m)
                    break

                elif i1 <= days[i+m+1]:
                    m += 1
                    i = i + m
                    print(i1, m, "a")
                    answer.append(m)
                    print(i, "i")
                    break

                elif i1 > days[i+m+1]:
                    m += 1
                    print(i1, m, "b")
                    continue

                else:
                    break

        return answer


a = [95, 90, 99, 99, 80, 99]
b = [1, 1, 1, 1, 1, 1]
print(aa.solution(a, b))


# 초본