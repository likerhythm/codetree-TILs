N = int(input())

arr = [list(input()) for _ in range(N)]

# 동전의 순서를 생산하는 재귀함수
# 순서 생산 후 탐색 횟수 계산하여 다음 함수에 넘겨준다.

start = [0, 0]
end = [0, 0]
nums = [[-1, -1] for _ in range(10)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S':
            start = [i, j]
        elif arr[i][j] == 'E':
            end = [i, j]
        elif arr[i][j] != '.':
            nums[int(arr[i][j])] = [i, j]

nums = [sublist for sublist in nums if sublist != [-1, -1]]

answer = [start] # 경로(좌표)
min_cnt = float('inf')

def calc_cnt(s, e): # s, e는 좌표값
    sx, sy = s
    ex, ey = e
    cnt = abs(sx - ex) + abs(sy - ey)
    return cnt

def f(previous, cnt):
    global min_cnt
    if len(answer) == 4:
        last_cnt = calc_cnt(answer[-1], end)
        cnt += last_cnt
        min_cnt = min(cnt, min_cnt)
        return
    for i in range(previous, len(nums)):
        answer.append(nums[i])
        temp = calc_cnt(answer[-2], answer[-1])# 횟수 계산
        f(i + 1, cnt + temp)
        answer.pop()

if len(nums) < 3:
    print(-1)
else:
    f(0, 0)
    print(min_cnt)