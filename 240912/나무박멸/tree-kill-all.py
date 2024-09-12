n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 나무, 벽 graph
kill_graph = [[0] * n for _ in range(n)] # 제초제 graph
walls = set()
for i in range(n):
    for j in range(n):
        if graph[i][j] == -1:
            walls.add((i, j))

KILL = -c - 1
WALL = -1

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def grow(): # 나무 성장
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                cnt = 0
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if in_range(nx, ny) and graph[nx][ny] > 0:
                        cnt += 1
                graph[x][y] += cnt


def breed(): # 나무 번식
    temp_graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_graph[i][j] = graph[i][j]
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                cnt = 0
                target = []
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy
                    if in_range(nx, ny) and graph[nx][ny] == 0 and kill_graph[nx][ny] == 0:
                        target.append([nx, ny])
                        cnt += 1
                if cnt > 0:
                    value = graph[x][y] // cnt
                    for nx, ny in target:
                        temp_graph[nx][ny] += value
    for i in range(n):
        for j in range(n):
            graph[i][j] = temp_graph[i][j]


kill_x = [-1, -1, 1, 1]
kill_y = [-1, 1, 1, -1]

def count_kill(x, y):
    cnt = graph[x][y]
    ignore = set()
    for i in range(1, k + 1):
        for j in range(4):
            if j in ignore:
                continue
            dx, dy = kill_x[j], kill_y[j]
            nx = x + dx * i
            ny = y + dy * i
            if in_range(nx, ny) and graph[nx][ny] > 0:
                cnt += graph[nx][ny]
            else:
                ignore.add(j)
    # print(f'kill {x},{y} = {cnt}')
    return cnt



def kill(): # 제초제
    max_cnt = 0
    result_x = 0
    result_y = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] > 0:
                cnt = count_kill(x, y)
                if max_cnt < cnt:
                    max_cnt = cnt
                    result_x, result_y = x, y
    # result에 제초제 뿌리기
    ignore = set()
    # print(f'kill {result_x}, {result_y}')
    kill_graph[result_x][result_y] = KILL
    for i in range(1, k + 1):
        for j in range(4):
            if j in ignore:
                continue
            dx, dy = kill_x[j], kill_y[j]
            nx = result_x + dx * i
            ny = result_y + dy * i
            if in_range(nx, ny):
                if graph[nx][ny] == 0 or (nx, ny) in walls: # 빈 공간이거나 벽인 경우
                    kill_graph[nx][ny] = KILL
                    ignore.add(j)
                elif graph[nx][ny] > 0 : # 나무인 경우
                    kill_graph[nx][ny] = KILL
    for i in range(n):
        for j in range(n):
            if kill_graph[i][j] < 0 and (i, j) not in walls:
                graph[i][j] = 0
                
    return max_cnt

def print_graph():
    for i in range(n):
        print(*graph[i])
    # print()

answer = 0
# print_graph()
for _ in range(m):
    for i in range(n):
        for j in range(n):
            if kill_graph[i][j] < 0:
                kill_graph[i][j] += 1
    
    # print('grow')
    grow()
    # print_graph()
    # print('breed')
    breed()
    # print_graph()
    # print('kill')
    answer += kill()
    # print_graph()

print(answer)