from collections import deque

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

q = deque([[0, 0]])
visited[0][0] = True



while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append([nx, ny])

print(1 if visited[n - 1][m - 1] else 0)