class aa:
    def solution(bridge_length, weight, truck_weights):
        bri_len = bridge_length
        bri_wei = weight
        truck_wei = truck_weights
        on_bri_tru = []
        total_wei = 0
        time = 0
        tt = 0
        while time <= 100000:
            if tt + bri_len == time and len(on_bri_tru) > 1:
                total_wei -= on_bri_tru.pop(0)[0]
                tt = on_bri_tru[0][1]
                print("pop",on_bri_tru,truck_wei,time,tt)
                continue

            elif len(truck_wei) != 0 and bri_wei >= total_wei + truck_wei[0]:
                total_wei += truck_wei[0]
                on_bri_tru.append([truck_wei.pop(0), time])
                time += 1
                tt = on_bri_tru[0][1]
                print("add",on_bri_tru,truck_wei,time,tt)
                continue

            elif len(truck_wei) == 0 and len(on_bri_tru) == 0 and tt + bri_len == time:
                time += 1
                print(on_bri_tru)
                print("end")
                break

            elif tt + bri_len == time and len(on_bri_tru) == 1:
                tt = on_bri_tru[0][1]
                total_wei -= on_bri_tru.pop(0)[0]
                print("pop2",on_bri_tru,truck_wei,time,tt)
                continue

            elif bri_wei >= total_wei:
                time += 1
                print("con",on_bri_tru,truck_wei,time)
                continue

            else:
                print(truck_wei, on_bri_tru, time, tt)
                print("dead")
                break

        print(time)
        print(truck_wei, on_bri_tru, total_wei, time, tt)
        answer = time
        return answer

aaa = 100
bbb = 100
ccc = [10,10,10,10,10,10,10,10,10,10,10]
print(aa.solution(aaa,bbb,ccc))
###################### 시간의 최댓값을 정해놓은 것이 값이 작아서 에러발생 ㅋㅋㅋㅋㅋㅋㅋㅋ ##############