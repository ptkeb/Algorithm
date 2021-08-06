
class aa:
    def solution(prices):
        answer = []
        for i in range(len(prices)):
            count = 0
            for m in range(len(prices) - i):
                 if i + m == len(prices) - 1:
                    answer.append(count)
                    break

                 elif prices[i] <= prices[i + m]:
                    count = count + 1

                 else:
                    answer.append(count)
                    break
        return answer

prices = [1, 2, 3, 2, 3]
print(aa.solution(prices))


# 정확도 66.7 효율성 6.7 총점 73.3/100
# 정확한 값으로 나오지만 시간이 너무 오래걸림. 
# for문의 반복사용으로 인한 것이므로 이것을 단축하는 과정이 필요
