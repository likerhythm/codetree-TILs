# 의자 앞에 여러개의 회전초밥 가능
# 1초에 한 칸씩 시계방향으로 회전
# 자신의 이름이 적혀있는 초밥 먹음
# 초밥 회전 -> 초밥 올리기 -> 초밥 먹기 -> 사진촬영

from collections import defaultdict as dfd

#벨트 길이, 명령 수
L, Q = map(int, input().split())
belt = [[] for _ in range(L)]
#time = t일때 belt 인덱스는 x = x - t(x-t==-1이면 x-t = L-1)
time = 0
customer = {}

def eat():
    #초밥 먹기
    keyToDel = []
    for key in customer.keys():
        x = customer[key]['x']
        index = x - t%L
        if index < 0:
            index = L - (t%L-x)
        #본인 초밥이 있으면 먹기
        while key in belt[index]:
            belt[index].remove(key)
            customer[key]['n'] -= 1
            # print("eat")
            #다 먹은 경우 퇴장
            if customer[key]['n'] == 0:
                keyToDel.append(key)
                # print("del")
    for k in keyToDel:
        del(customer[k])



for _ in range(Q):
    param = list(map(str, input().split()))
    method, t = param[0], int(param[1])
    
    #초밥 회전
    while t != time:
        time += 1
        eat()
    eat()
    # print("time:", time)
    # print("belt:", belt)
    # print("customer:", customer)

    match method:
        #초밥 올리기
        case '100':
            x, name = int(param[2]), param[3]
            index = x - t%L
            if index < 0:
                index = L - (t%L-x)
            belt[index].append(name)
            eat()
        #손님 입장
        case '200':
            x, name, n = int(param[2]), param[3], int(param[4])
            customer[name] = {'x': x, 'n': n}
            eat()
        #사진 촬영
        case '300':
            sushi = 0
            for arr in belt:
                sushi += len(arr)
            print(len(customer), sushi)