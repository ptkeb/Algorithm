
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
