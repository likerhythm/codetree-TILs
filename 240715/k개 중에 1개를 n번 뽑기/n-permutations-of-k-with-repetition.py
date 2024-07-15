K, N = map(int, input().split())

answer = [1, 1]

def print_num(curr_num):
    if curr_num == N:
        print(*answer)
        return
    for i in range(1, K + 1):
        answer[curr_num] = i
        print_num(curr_num + 1)

print_num(0)