# dp[i][j]: i번째 계단을 올라왔고, 지금까지 한 칸 올라간 횟수가 j+1번인 경우 최대 동전 개수

import sys
INT_MIN = -sys.maxsize

n = int(input())
coins = [0] + list(map(int, input().split()))

dp = [[INT_MIN] * 4 for _ in range(n + 1)]

dp[1][1] = coins[1]
dp[2][0] = coins[2]
dp[2][2] = coins[1] + coins[2]
if n > 2:
    dp[3][1] = max(dp[1][1], dp[2][0]) + coins[3]
    dp[3][3] = coins[1] + coins[2] + coins[3]
    for i in range(4, n + 1):
        dp[i][0] = dp[i - 2][0] + coins[i]
        dp[i][1] = max(dp[i - 2][1], dp[i - 1][0]) + coins[i]
        dp[i][2] = max(dp[i - 2][2], dp[i - 1][1]) + coins[i]
        dp[i][3] = max(dp[i - 2][3], dp[i - 1][2]) + coins[i]
print(max(dp[-1]))