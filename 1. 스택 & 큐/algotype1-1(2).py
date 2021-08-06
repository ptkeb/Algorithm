
class aa:
    def solution(prices):
        answer = []
        for i in range(len(prices)):
            count = 0
            b = prices.pop(0)
            c = int(b)
            for m in range(len(prices)):
                 if m == len(prices)-1:
                    answer.append(count)
                    break

                 elif c <= prices[m]:
                    count = count + 1

                 else:
                    count = count + 1
                    answer.append(count)
                    break
        return answer

prices = [1, 2, 3, 2, 3]
print(aa.solution(prices))


