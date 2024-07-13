# 아주 오랜 시간이 흐른 후 -> 연속 2n
import sys
input = sys.stdin.readline

T = int(input())

direction = {
    'U': 0,
    'L': 1,
    'R': 2,
    'D': 3,
}

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

for _ in range(T):
    N, M = map(int, input().split())
    
    marbles = []
    for _ in range(M):
        x, y, d = input().split()
        marbles.append([int(x) - 1, int(y) - 1, direction[d]])

    print_arr = [[[0, 0] for _ in range(N)] for _ in range(N)]

    marble_cnt = M
    has_conflict = False
    task = 0
    while True:
        has_conflict = False
        arr = [[[] for _ in range(N)] for _ in range(N)]
        print_arr = [[[0, 0] for _ in range(N)] for _ in range(N)]
        conflict_arr = []
        # 구슬 이동
        for i in range(len(marbles)):
            x, y, d = marbles[i]
            if d == -1: # 제거된 구슬일 경우
                continue
            nx = x + dxs[d]
            ny = y + dys[d]
            if in_range(nx, ny, N):
                if len(arr[nx][ny]) > 0:          #이미 구슬이 칸을 점유하는 경우
                    conflict_arr.append([nx, ny]) # 충돌 칸 저장
                    has_conflict = True
                    task = 0
                arr[nx][ny].append(i) # 해당 칸에 구슬의 index 추가
                marbles[i] = [nx, ny, d]
            else: # 방향 전환
                if len(arr[x][y]) > 0:          # 이미 구슬이 칸을 점유하는 경우
                    conflict_arr.append([x, y]) # 충돌 칸 저장
                    task = 0
                arr[x][y].append(i)
                marbles[i] = [x, y, 3 - d]
        # 구슬 제거
        for x, y in conflict_arr:
            conflict_marbles = arr[x][y]
            for i in conflict_marbles:
                marbles[i][2] = -1 # 구슬 제거    
                marble_cnt -= 1
        
        if not has_conflict:
            task += 1
        
        if task > 2 * N + 2:
            break
    print(marble_cnt)