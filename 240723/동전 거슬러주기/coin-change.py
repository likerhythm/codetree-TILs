N, M = map(int, input().split())

coins = list(map(int, input().split()))
dp = [float('inf')] * (M + 1)
for coin in coins:
    if coin <= M:
        dp[coin] = 1

min_coin = min(coins)

for i in range(min_coin + 1, M + 1):
    for coin in coins:
        if i - coin < min_coin:
            continue
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])