import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    input_list = list(map(int, input().split()))
    for j in range(n):
        arr[i][j].append(input_list[j])

num_index = [[] for _ in range(n * n + 1)]

for i in range(n):
    for j in range(n):
        num = arr[i][j][0]
        num_index[num] = [i, j, 0]

num_order = list(map(int, input().split()))

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def print_arr(arr):
    for i in range(n):
        print(*arr[i])

for num in num_order:
    x, y, index = num_index[num]
    max_num = 0
    rx = 0 # result x
    ry = 0 # result y
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and len(arr[nx][ny]) > 0 and max_num < max(arr[nx][ny]):
            max_num = max(arr[nx][ny])
            rx, ry = nx, ny

    if max_num == 0:
        continue
    
    # print(f'num={num}')
    # index 수정
    new_index = len(arr[rx][ry])
    for i in range(len(arr[x][y][index:])):
        temp = arr[x][y][index + i]
        num_index[temp] = [rx, ry, new_index + i]
        # print(f'num_index[{temp}]=[{rx}, {ry}, {new_index+i}]')

    # 숫자들 옮기기
    arr[rx][ry].extend(arr[x][y][index:])
    arr[x][y] = arr[x][y][:index]
    
    
    # print(num_index[4])
    # print_arr(arr)

for i in range(n):
    for j in range(n):
        len_arr = len(arr[i][j])
        if len_arr == 0:
            print(None)
        else:
            for k in range(len_arr - 1, -1, -1):
                print(arr[i][j][k], end=" ")
            print()