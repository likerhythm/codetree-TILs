n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

#구슬 위치 세팅
count = [[0] * n for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    count[r - 1][c - 1] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(t):
    next_count = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if count[x][y] == 1:
                max_x = 0
                max_y = 0
                max_num = 0
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if in_range(nx, ny) and max_num < arr[nx][ny]:
                        max_x = nx
                        max_y = ny
                        max_num = arr[nx][ny]
                next_count[max_x][max_y] += 1
    for i in range(n):
        for j in range(n):
            if next_count[i][j] > 1:
                m -= next_count[i][j]
                next_count[i][j] = 0
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

print(m)