n = int(input())

dp = [0] * (n + 1)

dp[2] = 1
if n > 2:
    dp[3] = 1
    for i in range(4, n + 1):
        if dp[i - 2] > 0:
            dp[i] += dp[i - 2]
        if dp[i - 3] > 0:
            dp[i] += dp[i - 3]
        dp[i] %=10007
print(dp[-1])