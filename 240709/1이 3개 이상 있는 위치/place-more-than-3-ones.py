n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y <n

result = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1
print(result)