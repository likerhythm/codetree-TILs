from collections import deque
import sys
import copy
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

removes = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            removes.append([i, j])
selected_removes = [[0, 0]] * k

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def bfs():
    visited = [[-1] * n for _ in range(n)]
    q = deque([[r1 - 1, c1 - 1]])
    visited[r1 - 1][c1 - 1] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and arr[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])
    return visited[r2 - 1][c2 - 1]

min_time = float('inf')
def do(curr, previous):
    global min_time
    if curr == k:
        for x, y in selected_removes:
            arr[x][y] = 0
        time = bfs()
        if time != -1:
            min_time = min(min_time, time)
        for x, y in selected_removes:
            arr[x][y] = 1
        return
    for i in range(previous, len(removes)):
        selected_removes[curr] = removes[i]
        do(curr + 1, i + 1)
    
do(0, 0)
print(min_time if min_time != float('inf') else -1)