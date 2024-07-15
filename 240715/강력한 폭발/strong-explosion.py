n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

bomb_index = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bomb_index.append([i, j])

range1_x = [-2, -1, 0, 1, 2]
range1_y = [0, 0, 0, 0, 0]
range2_x = [-1, 0, 0, 1, 0]
range2_y = [0, 1, 0, 0, -1]
range3_x = [-1, 1, 0, 1, -1]
range3_y = [1, 1, 0, -1, -1]

range_x = [range1_x, range2_x, range3_x]
range_y = [range1_y, range2_y, range3_y]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

bomb_type = [0 for _ in range(len(bomb_index))]

def get_score():
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(len(bomb_index)):
        x, y = bomb_index[i]
        type_index = bomb_type[i]
        for dx, dy in zip(range_x[type_index], range_y[type_index]):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
    return cnt
        
max_score = 0
def find_max(curr_num):
    global max_score
    if curr_num == len(bomb_index):
        max_score = max(max_score, get_score())
        return
    for i in range(3):
        bomb_type[curr_num] = i
        find_max(curr_num + 1)

find_max(0)
print(max_score)