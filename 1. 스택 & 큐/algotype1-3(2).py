class aa:
    def solution(bridge_length, weight, truck_weights):
        a = bridge_length
        b = weight
        c = truck_weights
        d = []
        e = 0  ## truck_weight_total
        f = 0  ## 경과시간
        g = [0]  ## 시간저장?

        if b > e + c[0]: # 트럭이 weight보다 무거우면 진행 안됨.
            tt = 0
            while f <100: # 완성시 무한에 가깝게 설정
                if len(c) == 0 and len(d) == 0:
                    print(d, c)
                    print("end")
                    break

                elif len(c) == 0 and f >= tt + a:
                    d.pop(0)
                    f+=
                    print("pop2", f, tt, d)
                    continue

                elif


        else:
            None





        answer = f
        return answer

aaa = 10
bbb = 30
ccc = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(aa.solution(aaa,bbb,ccc))