import sys
INT_MAX = sys.maxsize

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[INT_MAX] * N for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(N):
    dp[i][0] = min(arr[i][0], dp[i - 1][0])
    dp[0][i] = min(arr[0][i], dp[0][i - 1])

for i in range(1, N):
    for j in range(1, N):
        max_num = max(dp[i - 1][j], dp[i][j - 1])
        dp[i][j] = min(max_num, arr[i][j])

print(dp[-1][-1])