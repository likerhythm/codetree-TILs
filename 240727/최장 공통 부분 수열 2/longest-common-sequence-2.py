A = input()
B = input()
len_A = len(A)
len_B = len(B)
dp = [[''] * len_B for _ in range(len_A)]

if A[0] == B[0]:
    dp[0][0] = A[0]
for i in range(1, len_A):
    if A[i] == B[0]:
        dp[i][0] = B[0]
    else:
        dp[i][0] = dp[i - 1][0]
for i in range(1, len_B):
    if A[0] == B[i]:
        dp[0][i] = B[0]
    else:
        dp[0][i] = dp[0][i - 1]

def longger(str1, str2):
    if len(str1) > len(str2):
        return str1
    else:
        return str2

for i in range(1, len_A):
    for j in range(1, len_B):
        if A[i] == B[j]:
            dp[i][j] = dp[i - 1][j - 1] + A[i]
        else:
            dp[i][j] = longger(dp[i - 1][j], dp[i][j - 1])

print(dp[len_A - 1][len_B - 1])