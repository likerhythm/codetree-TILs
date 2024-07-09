n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(c)


mapper = {
    'U': 0,
    'D': 3,
    'R': 1,
    'L': 2,
}

direction = mapper[d]
dxs = [-1, 0, 0, 1]
dys = [0, 1, -1, 0]
x, y = r, c

def in_range(x, y):
    return 1 <= x < n + 1 and 1 <= y < n + 1

for _ in range(t):
    nx = x + dxs[direction]
    ny = y + dys[direction]
    
    if not in_range(nx, ny):
        direction = 3 - direction
    else:
        x, y = nx, ny

print(x, y)