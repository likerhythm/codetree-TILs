from collections import deque
import sys
input = sys.stdin.readline

# k: 시작점 수
# m: 치워야 할 돌의 개수
n, k, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

start_points = []
for _ in range(k):
    start_points.append(list(map(int, input().split())))

block_points = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            block_points.append([i, j])

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

remove = [] #  제거할 돌 목록

def bfs(x, y, visited):
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


# 0 ~ len(block_points)-1 중 m개 선택

max_cnt = 0
def set_remove():
    if len(remove) == m:
        visited = [[False] * n for _ in range(n)]
        for x, y in start_points:
            cnt += bfs(x, y, visited) # bfs
        max_cnt = max(max_cnt, cnt)
        return
    for i in range(len(block_points)):
        remove.append(i)
        set_remove()
        remove.pop()

    
set_remove()
print(max_cnt)