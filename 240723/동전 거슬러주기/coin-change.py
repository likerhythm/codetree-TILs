N, M = map(int, input().split())

coins = list(map(int, input().split()))
dp = [float('inf')] * (M + 1)
for coin in coins:
    dp[coin] = 1

for i in range(min(coins) + 1, M + 1):
    for coin in coins:
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[-1])