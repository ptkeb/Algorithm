class aa:
    def solution(bridge_length, weight, truck_weights):
        a = bridge_length
        b = weight
        c = truck_weights
        ## 트럭의 무게는 리스트
        # 따라서 b보다 c[0]이 작으면, 트럭 리스트를 pop(0)하여 새로운 큐d에 집어넣는다.
        # 큐 d 안의 트럭 무게의 총합 e이 b를 넘을경우 더이상 추가하지 못한다.
        # 트럭은 a초 경과후 나갈수있으므로  이를 기록해야함.
        # a초를 경과한 트럭은 큐 d에서 빠지게되므로(pop(0)),
        ### 비효율적으로 생각되는 방법 : 초단위로 위의 과정이 일어나게 만들어서 과정이 완료된 초를 기록
        ### 이것을 좀더 효율적으로 사용할 방법 : 다리가 비어지고, 새로운 트럭이 추가될때, 시간도 같이 추가되게.
        # 이후 큐 d에 후속 트럭이 추가된다.
        # 마지막으로 나가는 시간 추가를 위해 +1 <-- 조건 확실하게해서
        # 다리를 지나는 트럭이 없으면 알고리즘 종료
        ## 첫번째는 비효율적이라도 제대로하는것으로 시작
        d = []
        e = 0 ## truck_weight_total
        f = 0 ## 경과시간
        g = [0] ## 시간저장?

        if b > e + c[0]:
            tt = 0
            while f <= 100:
                if len(c) == 0 and len(d) == 0:
                    print(d,c)
                    print("end")
                    break

                elif len(c) == 0 and f >= tt + a:
                    tt = int(g.pop(0))
                    d.pop(0)
                    print("pop2",f, tt, g, d)
                    continue

                elif len(c) == 0 and f >= tt + a and len(g) == 0:
                    d.pop(0)
                    print("pop3",f, tt, d)
                    continue

                elif len(c) != 0 and e + c[0] <= b:
                    d.append(c.pop(0))
                    e += d[0]
                    g.append(f)
                    tt = int(g.pop(0))
                    f += 1
                    print("add", f, g)
                    print(d, c)
                    continue

                elif f == tt + a:
                    e -= d[0]
                    d.pop(0)
                    print("pop",f,tt)
                    print(d,c)    ## 트럭이 지나간 시간마다 팝
                    continue

                elif len(c) != 0 and e + c[0] > b:
                    f += 1
                    print("con", f, g)
                    print(d,c)
                    continue

                else:
                    print("dead", d)
                    break
            print(f)
            print(g)
        answer = f
        return answer

aaa = 10
bbb = 30
ccc = [10,10,10,10,10,10,10,10,10,10]
print(aa.solution(aaa,bbb,ccc))
## 실패. 표본으로 이용해서 다시 짜야됨