N, M = map(int, input().split()) # N개의 옷, M일

clothes = [list(map(int, input().split())) for _ in range(N)] # s(시작), e(끝), v(만족도)순으로 입력

# dp[i][j]: i일에 j옷을 입었을 때의 최대 만족도
dp = [[0] * N for _ in range(M + 1)]

value_diff = [[0] * N for _ in range(N)] # value_diff[i][j]: i번 옷을 입은 후 j번 옷을 입을 때 가치 차이
for i in range(N):
    for j in range(N):
        value_diff[i][j] = abs(clothes[i][2] - clothes[j][2])

for i in range(2, M + 1): # i번째 날
    for j in range(N): # j번 옷을 입었을 때 최대 만족도
        for k in range(N): # 전날 k번 옷을 입은 경우
            s_k, e_k, v_k = clothes[k]
            s_j, e_j, v_j = clothes[j]
            if s_k <= i - 1 <= e_k and s_j <= i <= e_j:
                dp[i][j] = max(dp[i - 1][k] + value_diff[k][j], dp[i][j])

print(max(dp[-1]))