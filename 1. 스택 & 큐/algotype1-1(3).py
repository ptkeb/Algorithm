
class aa:
    def solution(prices):
        answer = []
        
        for i in range(len(prices)):
            count = 0
            pr = prices.pop(0)
            a = int(pr)

            for m in range(len(prices)):
                if m == len(prices)-1:
                    count += 1
                    answer.append(count)
                    print(a,i,m,"펑")
                    print(prices)
                    break

                elif a <= prices[m]:
                    count += 1
                    print(a,i,m,"추가")
                    print(prices)
                    
                else:
                    count += 1
                    answer.append(count)
                    print(a,i,m,"하락")
                    print(prices)
                    break

        answer.append(0)
        return answer

prices = [1, 2, 3, 2, 3]
print(aa.solution(prices))


# 코드 돌아가는 방식을 알기위한 로그작업
