K, N = map(int, input().split())

answer = [1 for _ in range(N)]

def print_num(curr):
    if curr == N:
        print(*answer)
        return
    for i in range(1, K + 1):
        if curr > 1 and answer[curr - 1] == i and answer[curr - 2] == i:
            continue
        answer[curr] = i
        print_num(curr + 1)

print_num(0)