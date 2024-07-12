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

    arr = [[[0, 0]] * N for _ in range(N)]

    for _ in range(M):
        x, y, d = input().split()
        x = int(x)
        y = int(y)
        arr[x - 1][y - 1] = [1, direction[d]]

    count = 0
    while True:
        next_arr = [[[0, 0] for _ in range(N)] for _ in range(N)]
        # 구슬 이동
        for x in range(N):
            for y in range(N):
                if arr[x][y][0] == 1:
                    d = arr[x][y][1]
                    nx = x + dxs[d]
                    ny = y + dys[d]
                    if in_range(nx, ny, N):
                        next_arr[nx][ny][0] += 1
                        next_arr[nx][ny][1] = d
                    else: # 방향 전환
                        next_arr[x][y][0] += 1
                        next_arr[x][y][1] = 3 - d
        
        # 충돌 감지
        has_conflict = False
        for x in range(N):
            for y in range(N):
                if next_arr[x][y][0] > 1: # 충돌이 발생한 경우
                    next_arr[x][y][0] = 0
                    has_conflict = True
                    count = 0
                arr[x][y] = next_arr[x][y]

        if not has_conflict:
            count += 1
        if count > 2 * N + 2:
            break
    answer = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y][0] == 1:
                answer += 1
    print(answer)