n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 오른쪽, 아래 순
dxs = [0, 1]
dys = [1, 0]

found = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if arr[x][y] == 0: # 뱀이 있는 경우
        return False
    if visited[x][y]:
        return False
    return True

def dfs(x, y):
    global found
    if x == n - 1 and y == m - 1:
        found = True
        return
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)
  

visited[0][0] = True
dfs(0, 0)
if found:
    print(1)
else:
    print(0)