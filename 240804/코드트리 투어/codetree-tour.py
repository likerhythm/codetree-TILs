from collections import deque
import sys

INT_MAX = sys.maxsize

Q = int(input())
command = list(map(int, input().split()))
n, m = command[1], command[2]
edges = command[3:]
graph = [[-1] * n for _ in range(n)]
start_node = 0

for i in range(0, len(edges), 3):
    v, u, w = edges[i:i + 3]
    if graph[v][u] != -1:
        w = min(graph[v][u], w)
    graph[v][u] = w
    graph[u][v] = w

travel_dict = {} # 여행상품리스트
removed_set = set() # 취소된 여행상품 set

def bfs(dest):
    q = deque([start_node])
    visited = [INT_MAX] * n
    visited[start_node] = 0
    while q:
        v = q.popleft()
        for nv in range(n):
            cost = graph[v][nv]
            if cost > -1 and visited[nv] > visited[v] + cost:
                visited[nv] = visited[v] + cost
                q.append(nv)
    return visited[dest]

def code200(command):
    id_, revenue, dest = command[1:]
    cost = bfs(dest)
    travel_dict[id_] = [revenue, dest, cost]

def code300(command):
    id_ = command[1]
    if id_ in travel_dict:
        removed_set.add(id_)

def code400():
    max_value = -1
    result_id = 0
    sorted_key = []
    for key in travel_dict:
        sorted_key.append(key)
    sorted_key.sort()
    for key in sorted_key:
        if key in removed_set:
            continue
        revenue, dest, cost = travel_dict[key]
        if max_value < revenue - cost:
            max_value = revenue - cost
            result_id = key
    if max_value == -1:
        print(-1)
    else:
        print(result_id)
        removed_set.add(result_id)

def code500(command):
    global start_node
    start_node = command[1]
    for key in travel_dict:
        revenue, dest, cost = travel_dict[key]
        travel_dict[key][2] = bfs(dest)

for _ in range(Q - 1):
    command = list(map(int, input().split()))
    code = command[0]
    if code == 200:
        code200(command)
    elif code == 300:
        code300(command)
    elif code == 400:
        code400()
    elif code == 500:
        code500(command)