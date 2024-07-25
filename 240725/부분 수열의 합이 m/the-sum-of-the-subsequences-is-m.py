import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())

coins = list(map(int, input().split()))
dp = [INT_MAX] * (m + 1)
dp[0] = 0

for coin in coins:
    for i in range(m, coin - 1, -1):
        if i - coin >= 0 and dp[i - coin] != INT_MAX:
            dp[i] = min(dp[i - coin] + 1, dp[i])

if dp[-1] == INT_MAX:
    print(-1)
else:
    print(dp[-1])