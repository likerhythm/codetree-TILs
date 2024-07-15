n = int(input())

answer = [0 for _ in range(n)]
visited = [False for _ in range(n + 1)]

def print_per(curr):
    if curr == n:
        print(*answer)
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        answer[curr] = i
        visited[i] = True
        print_per(curr + 1)

        visited[i] = False

print_per(0)