from collections import deque
import sys
import copy
input = sys.stdin.readline

# k: 시작점 수
# m: 치워야 할 돌의 개수
n, k, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

start_points = []
for _ in range(k):
    x, y = map(int, input().split())
    start_points.append([x - 1, y - 1])

block_points = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            block_points.append([i, j])

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

remove = [] #  제거할 돌의 block_points index


def before_bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                q.append([nx, ny])
                cnt += 1
    return cnt


def can_go(x, y):
    return arr[x][y] == 0 or ([x, y] in remove)

def after_bfs(x, y, temp_visited):
    q = deque([[x, y]])
    if temp_visited[x][y] == True:
        cnt = 0
        return 0
    else:
        temp_visited[x][y] = True
        cnt = 1
    found = False
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and temp_visited[nx][ny]: # 고립된 공간이 아닌 경우
                found = True
            if 0 <= nx < n and 0 <= ny < n and not temp_visited[nx][ny] and can_go(nx, ny): # 
                temp_visited[nx][ny] = True
                q.append([nx, ny])
                cnt += 1
    if found:
        return cnt
    else: # 고립된 공간인 경우
        return 0


# 0 ~ len(block_points)-1 중 m개 선택
max_cnt = 0
def set_remove(previous):
    global after_cnt
    after_cnt = 0
    global max_cnt
    if len(remove) == m:
        temp_visited = copy.deepcopy(visited)
        for x, y in remove:
            if not visited[x][y]:
                after_cnt += after_bfs(x, y, temp_visited)
        max_cnt = max(max_cnt, after_cnt)
        
        # print(f'remove={remove}')
        # for i in range(n):
        #     print(*temp_visited[i])
        # print(f'after_cnt={after_cnt}')
        # print()
        return
    for i in range(previous + 1, len(block_points)):
        remove.append(block_points[i])
        set_remove(i)
        remove.pop()

# 시작점으로부터 우선 탐색
before_cnt = 0
for x, y in start_points:
    if not visited[x][y]:
        before_cnt += before_bfs(x, y)
set_remove(-1) # 제거한 돌에서부터 bfs

print(before_cnt + max_cnt)