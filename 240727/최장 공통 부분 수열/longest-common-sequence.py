A = input()
B = input()
len_A = len(A)
len_B = len(B)

dp = [[0] * len_B for _ in range(len_A)] # dp[i][j]: A의 i번째, B의 j번째 문자까지 고려하였을 때 최장공통부분수열
if A[0] == B[0]:
    dp[0][0] = 1
for i in range(len_A):
    if B[0] == A[i]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i - 1][0]
    if A[0] == B[i]:
        dp[0][i] = 1
    else:
        dp[0][i] = dp[0][i - 1]

for i in range(1, len_A):
    for j in range(1, len_B):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len_A - 1][len_B - 1])