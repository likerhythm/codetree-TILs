from collections import deque
import operator

N = int(input())

visited = [-1] * (N + 10)

op = {
    0: operator.sub,
    1: operator.add,
    2: operator.floordiv,
    3: operator.floordiv, 
}
dxs = [1, 1, 2, 3]

def bfs():
    q = deque([N])
    visited[N] = 0
    while(q):
        x = q.popleft()
        for i in range(4):
            if i == 2 and x % 2 > 0:
                continue
            elif i == 3 and x % 3 > 0:
                continue
            nx = op[i](x, dxs[i])
            # print(f'{x}와 {dxs[i]}를 op[{i}] 연산, 그 결과 nx={nx}')
            if 0 <= nx < N + 10 and (visited[nx] == -1 or visited[nx] > visited[x] + 1):
                visited[nx] = visited[x] + 1
                if nx == 1:
                    return
                q.append(nx)
bfs()
# print(visited)
print(visited[1])