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
                    print(a1[i], m)
                    continue
                else:
                    days.append(m-1)
                    print("a")
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


a = [1, 0, 0, 0, 0, 0, 0]
b = [1, 1, 2, 3, 45, 1, 2]
print(aa.solution(a, b))


# 정확도 63.6 통과 못함
# ?? progress를 제대로 인식하지 않음.

# queue로 바꾸는 작업을 해야할듯
