# dfs 시간복잡도: N*M
# 100번 반복
import sys
sys.setrecursionlimit(3000)


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
max_height = 0 # 마을에서 가장 높이가 높은 집의 높이
for i in range(N):
    for j in range(M):
        if max_height < arr[i][j]:
            max_height = arr[i][j]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def dfs(x, y, k):
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] > k:
            visited[nx][ny] = True
            dfs(nx, ny, k)

answer_cnt = 0
answer_k = 1
for k in range(1, max_height):
    cnt = 0 # 안전 영역의 수
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] > k:
                visited[i][j] = True
                cnt += 1
                dfs(i, j, k)
    if answer_cnt < cnt:
        answer_cnt = cnt
        answer_k = k
print(answer_k, answer_cnt)