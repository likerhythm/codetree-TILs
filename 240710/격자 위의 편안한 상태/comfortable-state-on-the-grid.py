N, M = map(int, input().split())

points = []

for _ in range(M):
    x, y = list(map(int, input().split()))
    x -= 1
    y -= 1
    points.append([x, y])

arr = [[0] * N for _ in range(N)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for x, y in points:
    arr[x][y] = 1
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)