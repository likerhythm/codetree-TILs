# dp[i][j]: i번째 계단을 올라왔고, 지금까지 한 칸 올라간 횟수가 j번인 경우 최대 동전 개수

import sys
INT_MIN = -sys.maxsize

n = int(input())
coins = list(map(int, input().split()))

dp = [[INT_MIN] * 3 for _ in range(n)]
dp[0][1] = coins[0]
dp[1][0] = coins[1]
dp[1][2] = coins[0] + coins[1]
for i in range(2, n):
    dp[i][0] = dp[i - 2][0] + coins[i]
    dp[i][1] = max(dp[i - 2][1], dp[i - 1][0]) + coins[i]
    dp[i][2] = max(dp[i - 2][2], dp[i - 1][1]) + coins[i]
print(max(dp[-1]))