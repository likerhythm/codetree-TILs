n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

# 오른쪽(0), 아래쪽(1), 왼쪽(2), 위쪽(3)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
direction = 0

x, y = 0, 0
num = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

while True:
    arr[x][y] = num
    if num == n * m:
        break

    nx = x + dxs[direction]
    ny = y + dys[direction]

    # 회전해야 하는 경우
    if not (in_range(nx, ny) and arr[nx][ny] == 0):
        direction = (direction + 1) % 4
    else:
        x, y = nx, ny
        num += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()