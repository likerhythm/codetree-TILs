# 의자 앞에 여러개의 회전초밥 가능
# 1초에 한 칸씩 시계방향으로 회전
# 자신의 이름이 적혀있는 초밥 먹음
# 초밥 회전 -> 초밥 올리기 -> 초밥 먹기 -> 사진촬영

from collections import defaultdict as dfd

#벨트 길이, 명령 수
L, Q = map(int, input().split())
belt = {}
#time = t일때 belt 인덱스는 x = x - t(x-t==-1이면 x-t = L-1)
time = 0
customer = {}
sushiSet = set()

def eat():
    if belt != {}:
        #초밥 먹기
        customerToDel = []
        beltToDel = []
        for key in customer.keys():
            x = customer[key]['x']
            index = x - t%L
            if index < 0:
                index = L - (t%L-x)
            #본인 초밥이 있으면 먹기
            index = str(index)
            # print(index, index in belt)
            if index in belt:
                while key in belt[index]:
                    #초밥 먹기
                    belt[index][key] -= 1
                    if belt[index][key] == 0:
                        del(belt[index][key])
                    #한 칸에 있는 초밥 모두 먹은 경우
                    if not belt[index]:
                        beltToDel.append(index)
                    customer[key]['n'] -= 1
                    print("eat")
                    #다 먹은 경우 퇴장
                    if customer[key]['n'] == 0:
                        customerToDel.append(key)
                        print("del")
        for k in customerToDel:
            del(customer[k])
        for b in beltToDel:
            del(belt[b])



for _ in range(Q):
    param = list(map(str, input().split()))
    method, t = param[0], int(param[1])
    print(method)
    #초밥 회전
    if belt == {} or customer == {}:
        time = t
        print(time)
    else:
        while t != time:
            time += 1
            print(time)
            eat()
            print("belt:", belt)
            print("customer:", customer)
            if 
    eat()
    # print("time:", time)
    # print("belt:", belt)
    # print("customer:", customer)

    match method:
        #초밥 올리기
        case '100':
            x, name = int(param[2]), param[3]
            sushiSet.add(name)
            index = x - t%L
            if index < 0:
                index = L - (t%L-x)
            index = str(index)
            if index in belt:
                if name in belt[index]:
                    belt[index][name] += 1
                else:
                    belt[index][name] = 1
            else:
                belt[index] = {name: 1}
            eat()
        #손님 입장
        case '200':
            x, name, n = int(param[2]), param[3], int(param[4])
            customer[name] = {'x': x, 'n': n}
            eat()
        #사진 촬영
        case '300':
            print('300')
            sushi = 0
            for index in belt:
                for key in belt[index].keys():
                    sushi += belt[index][key]
            print(len(customer), sushi)