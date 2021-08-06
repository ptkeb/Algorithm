
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
# i와 m을 축으로하는 2차원 리스트

# 먼저 나오는 for문을 리스트를 이용한 과정으로 대체?
# 똑같이 2차원이기에 비슷한 결과가 나올듯

# prices[i]를 비교하는 방식을 다르게
# 밖의 for문 을 큐를 이용한것으로 대체. 즉 prices[0]를 계속 pop하여 사용하는 구문으로 만들기
# 결과 안좋음 ㅋㅋㅋㅋㅋ
# 추가적인 for문 사용없이 한개로 끝내여 될것 같은데 
