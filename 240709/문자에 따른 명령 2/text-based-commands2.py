in_str = input()
# 북(0), 동(1), 남(2), 서(3)
direction = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0

for i in range(len(in_str)):
    if in_str[i] == 'L':
        direction = (direction + 3) % 4
    elif in_str[i] == 'R':
        direction = (direction + 1) % 4
    else:
        x = x + dx[direction]
        y = y + dy[direction]

print(x, y)