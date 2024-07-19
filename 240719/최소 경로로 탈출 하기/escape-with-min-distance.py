from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

q = deque([[0, 0]])
visited[0][0] = 0

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

print(-1 if visited[n-1][m-1] == -1 else visited[n-1][m-1])