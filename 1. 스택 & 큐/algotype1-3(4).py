class aa:
    def solution(bridge_length, weight, truck_weights):
        a = bridge_length
        b = weight
        c = truck_weights
        d = []
        e = 0
        f = 0
        tt = 0
        while f <= 100000:
            if tt + a == f and len(d) > 1:
                e -= d.pop(0)[0]
                tt = d[0][1]
                print("pop",d,c,f,tt)
                continue

            elif len(c) != 0 and b >= e + c[0]:
                e += c[0]
                d.append([c.pop(0), f])
                f += 1
                tt = d[0][1]
                print("add","d-",d,"c-",c,"f-",f,"tt-",tt)
                continue

            elif len(c) == 0 and len(d) == 0 and tt + a == f:
                f += 1
                print(d)
                print("end")
                break

            elif tt + a == f and len(d) == 1:
                tt = d[0][1]
                e -= d.pop(0)[0]
                print("pop2",d,c,f,tt)
                continue

            elif b >= e:
                f += 1
                print("con",d,c,f)
                continue

            else:
                print(c, d, f, tt)
                print("dead")
                break

        print(f)
        print(c, d, e, f, tt)
        answer = f
        return answer

aaa = 100
bbb = 100
ccc = [10,10,10,10,10,10,10,10,10,10]
print(aa.solution(aaa,bbb,ccc))
## 정확도 92.9
# 문제는 아마도 지정되는 if 문의 조건때문인듯(2번째)
# 조건을 한개 못찾은듯