N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

x, y = 0, 0
max_cnt = 0


for i in range(N - 2):
    for j in range(N - 2):
        cnt = 0
        for k in range(3):
            for l in range(3):
                if arr[i + k][j + l] == 1:
                    cnt += 1
        max_cnt = max(max_cnt, cnt)

print(max_cnt)