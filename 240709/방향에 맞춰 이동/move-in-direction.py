N = int(input())
move = []
for _ in range(N):
    direction, count = map(str, input().split())
    move.append([direction, count])

direction = {
    'W': 0,
    'S': 1,
    'N': 2,
    'E': 3,
}
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
x, y = 0, 0

for i in range(N):
    direct, count = move[i]
    count = int(count)
    index = direction[direct]
    x = x + dx[index] * count
    y = y + dy[index] * count

print(x, y)