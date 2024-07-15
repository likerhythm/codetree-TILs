N, M = map(int, input().split())

# 길이 N의 이진수 중 1의 개수가 M개인 이진수 filter

answer = [0 for _ in range(N)]

def print_num(curr, cnt):
    if curr == N:
        if cnt == M:
            for i, x in enumerate(answer):
                if x == 1:
                    print(i + 1, end=' ')
            print()
            return
    else:
        answer[curr] = 1
        print_num(curr + 1, cnt + 1)
        answer[curr] = 0
        print_num(curr + 1, cnt)


print_num(0, 0)