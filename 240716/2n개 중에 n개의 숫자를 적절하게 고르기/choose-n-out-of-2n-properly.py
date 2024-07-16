n = int(input())

num_list = list(map(int, input().split()))

def calc():
    sum1 = 0
    for i in answer:
        sum1 += num_list[i]
    total_sum = sum(num_list)
    sum2 = total_sum - sum1
    return abs(sum2 - sum1)

# 0 ~ 2n-1의 수 중 n개 선택
min_r = float('inf')
answer = [0 for _ in range(n)]
def f(previous, curr):
    global min_r
    if curr == n:
        r = calc()# 합의 차 계산
        min_r = min(r, min_r)
        return
    for i in range(previous, 2 * n):
        answer[curr] = i
        f(previous + 1, curr + 1)

f(0, 0)
print(min_r)