N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [False] * (N + 1)
cnt = 0

def dfs(v):
    global cnt
    for nv in range(N + 1):
        edge = graph[v][nv]
        if edge == 1 and not visited[nv]:
            cnt += 1
            visited[nv] = True
            dfs(nv)

visited[1] = True
dfs(1)
print(cnt)