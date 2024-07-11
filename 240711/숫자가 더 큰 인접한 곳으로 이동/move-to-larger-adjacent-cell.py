n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

x = r - 1
y = c - 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

found = True
while found:
    found = False
    now = arr[x][y]
    print(now, end=' ')
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and arr[nx][ny] > now:
            x, y = nx, ny
            found = True
            break