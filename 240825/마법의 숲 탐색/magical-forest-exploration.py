# <진행 순서>
# 1. 남쪽으로 한 칸 내려간다
# 2. 1의 방법으로 이동할 수 없으면 서쪽 방향으로 회전하면서 내려간다. -> 출구가 반시계로 회전
# 3. 1과 2의 방법으로 이동할 수 없으면 동쪽 방향으로 회전하면서 내려간다. -> 출구가 시계로 회전
# 4. 더이상 이동할 수 없으면 골렘을 따라 이동하며 가장 남쪽 칸으로 이동

# <조건>
# 골렘이 최대한 남쪽으로 이동해도 골렘의 몸 일부가 숲에서 벗어난 상태라면 해당 고렘을 포함해 숲에 위치한 모든 골렘을 제거하고 다음 골렘부터 다시 시작
# -> 단 몸 일부가 벗어난 고렘에 탑승한 정령이 도달하는 최종 위치를 답에 포함시키지 않음

import sys
sys.setrecursionlimit = 3000

R, C, K = map(int, input().split())
golems = []
for _ in range(K):
    golems.append([1] + list(map(int, input().split())))

EMPTY = 0
forest = [[EMPTY] * C for _ in range(R + 3)]

exit = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 골렘 중앙 기준으로 출구 위치


def can_go_south(r, c):
    in_range = 0 <= r < (R + 2) - 1 and 0 <= c < C - 1
    if in_range:
        no_golem = forest[r + 2][c] == EMPTY and forest[r + 1][c + 1] == EMPTY and forest[r + 1][c - 1] == EMPTY
        return no_golem
    return False

def can_go_west(r, c):
    in_range = r < R + 1 and c > 1
    if in_range:
        no_golem = forest[r - 1][c - 1] == EMPTY and forest[r][c - 2] == EMPTY and forest[r + 1][c - 1] == EMPTY and forest[r + 2][c - 1] == EMPTY and forest[r + 1][c - 2] == EMPTY
        return no_golem
    return False

def can_go_east(r, c):
    in_range = r < R + 1 and c < C - 2
    if in_range:
        no_golem = forest[r - 1][c + 1] == EMPTY and forest[r][c + 2] == EMPTY and forest[r + 1][c + 1] == EMPTY and forest[r + 1][c + 2] == EMPTY and forest[r + 2][c + 1] == EMPTY
        return no_golem
    return False
    
def go_west(r, c, d, num):
    global golems
    if d == 0:
        d = 3
    else:
        d -= 1
    golems[num][0] = r + 1
    golems[num][1] = c - 1
    golems[num][2] = d
    return r + 1, c - 1, d

def go_east(r, c, d, num):
    global golems
    if d == 3:
        d = 0
    else:
        d += 1
    golems[num][0] = r + 1
    golems[num][1] = c + 1
    golems[num][2] = d
    return r + 1, c + 1, d

def clear():
    for i in range(R + 3):
        for j in range(C):
            forest[i][j] = EMPTY

def set_neighbor(exit_r, exit_c, num):
    drs = [-1, 0, 1, 0] # 북, 동, 남, 서
    dcs = [0, 1, 0, -1]
    nei_set = set() # 이웃 골렘이 여러개인 경우를 고려
    for dr, dc in zip(drs, dcs): # 출구 주변에 인접한 골렘 확인
        nr = exit_r + dr
        nc = exit_c + dc
        if 0 <= nr < R + 3 and 0 <= nc < C:
            neighbor = forest[nr][nc]
            if neighbor > 0 and neighbor != num + 1 and tmp_forest[nr][nc] == 0:
                nei_set.add(neighbor) 
    # print(f'num={num}, nei_set={nei_set}')
    for nei in nei_set:
        nei_r, nei_c, nei_d = golems[nei - 1]
        tmp_forest[nei_r][nei_c] = 1
        for dr, dc in zip(drs, dcs):
            nr_ = nei_r + dr
            nc_ = nei_c + dc
            tmp_forest[nr_][nc_] = 1 # 이동 가능한 모든 구간을 1로 설정
        d = golems[nei - 1][2]
        nei_exit_r = nei_r + exit[d][0]
        nei_exit_c = nei_c + exit[d][1]
        set_neighbor(nei_exit_r, nei_exit_c, neighbor - 1)

answer = []
for num, golem in enumerate(golems):
    # 골렘 이동
    r, c, d = golem
    c = c - 1
    while can_go_south(r, c) or can_go_west(r, c) or can_go_east(r, c):
        if can_go_south(r, c):
            r += 1
            golems[num][0] = r
            golems[num][1] = c
            # print('go_south')
        elif can_go_west(r, c):
            r, c, d = go_west(r, c, d, num)
            # print('go_west')
        else:
            r, c, d = go_east(r, c, d, num)
            # print('go_east')
    if r <= 3:
        clear()
        continue
    else:
        forest[r][c] = num + 1
        forest[r - 1][c] = num + 1
        forest[r][c + 1] = num + 1
        forest[r + 1][c] = num + 1
        forest[r][c - 1] = num + 1
    
    # 정령 이동
    tmp_forest = [[EMPTY] * C for _ in range(R + 3)]
    tmp_forest[r][c] = 1
    tmp_forest[r - 1][c] = 1
    tmp_forest[r][c + 1] = 1
    tmp_forest[r + 1][c] = 1
    tmp_forest[r][c - 1] = 1
    exit_r = r + exit[d][0]
    exit_c = c + exit[d][1]
    # print(f'num={num}')
    set_neighbor(exit_r, exit_c, num)
    
    found = False
    for i in range(R + 2, -1, -1):
        for j in range(C):
            if tmp_forest[i][j] == 1:
                answer.append(i - 2)
                found = True
                break
        if found:
            break

    # for i in range(R + 3):
    #     print(*tmp_forest[i])
    # print()
            

    # for i in range(R + 3):
    #     print(*forest[i])
    # print()  
# print(answer)
print(sum(answer))