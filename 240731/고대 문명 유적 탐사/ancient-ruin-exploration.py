# 회전의 목표: 유물 1차 획득 가치 > 회전각도 작은 순 > 열이 작은 순 > 행이 작은 순
# 새로 생겨나는 조각: 열 번호가 작은 순 > 행 번호가 큰 순 => 왼쪽 아래에서 오른쪽 위 순

from collections import deque

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
pieces = list(map(int, input().split()))
pieces_cursor = 0


def bfs(temp_arr, visited, x, y):
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    origin_x = x
    origin_y = y
    q = deque([[x, y]])
    visited[x][y] = True
    removed = [[x, y]]
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and temp_arr[nx][ny] == temp_arr[x][y]:
                visited[nx][ny] = True
                q.append([nx, ny])
                removed.append([nx, ny])
                cnt += 1
    if cnt >= 3:
        return cnt, removed
    else:
        return 0, []

def calc_value(temp_arr):
    total_value = 0
    total_removed = []
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                value, removed = bfs(temp_arr, visited, i, j)
                total_value += value
                total_removed += removed
    return total_value, total_removed

def rotate(x, y, radius): # x, y를 기준으로 radius(90, 180, 270)만큼 회전(항상 회전해야 됨)
    temp_arr = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            temp_arr[i][j] = arr[i][j]
    for i in range(radius // 90):
        temp_first = temp_arr[x - 1][y - 1]
        temp_second = temp_arr[x][y - 1]
        temp_arr[x - 1][y - 1] = temp_arr[x + 1][y - 1]
        temp_arr[x][y - 1] = temp_arr[x + 1][y]
        temp_arr[x + 1][y - 1] = temp_arr[x + 1][y + 1]
        temp_arr[x + 1][y] = temp_arr[x][y + 1]
        temp_arr[x + 1][y + 1] = temp_arr[x - 1][y + 1]
        temp_arr[x][y + 1] = temp_arr[x - 1][y]
        temp_arr[x - 1][y + 1] = temp_first
        temp_arr[x - 1][y] = temp_second
    #유물 1차 획득 가치 계산
    total_value, total_removed = calc_value(temp_arr)
    return total_value, total_removed, temp_arr

def fill():
    global pieces_cursor
    for j in range(5):
        for i in range(4, -1, -1):
            if arr[i][j] == 0:
                arr[i][j] = pieces[pieces_cursor]
                pieces_cursor += 1

def print_arr():
    for i in range(5):
        print(*arr[i])

for k in range(K): # k번째 턴
    max_value = 0
    next_arr = []
    next_removed = []
    found = True
    result_radius = 0 # 최대 가치일 때 돌린 각도
    result_x = 0 # 최대 가치일 때 중심 x
    result_y = 0 # 최대 가치일 때 중심 y
    for radius in range(90, 271, 90):
        for i in range(1, 4): # 회전을 통해 최대 유물 가치 구하기
            for j in range(1, 4):
                total_value, total_removed, temp_arr = rotate(i, j, radius)
                if max_value < total_value:
                    max_value = total_value
                    next_arr = temp_arr
                    next_removed = total_removed
                    result_radius = radius
                    result_x = i
                    result_y = j
    if max_value == 0: # 더 이상 유물이 발견되지 않은 경우
        found = False
        break
    for x in range(5):
        for y in range(5):
            arr[x][y] = next_arr[x][y]
    for x, y in next_removed:
            arr[x][y] = 0
    # print_arr()
    # 빈 자리에 조각 채우기
    fill()

    while True:
        temp_arr = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                temp_arr[i][j] = arr[i][j]
        extra_value, extra_removed = calc_value(temp_arr)
        if extra_value == 0:
            break
        for x, y in extra_removed:
            arr[x][y] = 0
        max_value += extra_value
        fill()
    print(max_value, end=' ')
    # print_arr()
    # print(f'{k}턴 끝')
    # print()