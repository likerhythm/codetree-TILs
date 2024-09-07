# 노드 추가: 노드를 트리에 추가. pid == -1이면 루트 노드
# 색깔 변경: 서브트리의 모든 노드의 색을 변경한다.
# 색깔 조회: 특정 노드의 현재 색깔을 조회한다.
# 점수 조회: 모든 노드의 가치의 제곱의 합을 출력. 가치는 해당 노드를 루트로하는 서브트리의 서로 다른 색의 개수
# color - 1:빨강, 2:주황, 3:노랑, 4:초록, 5:파랑

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

node_info = [[0, 0] for _ in range(100001)] # color, maxdepth
parent_info = [0] * 100001 # pid
child_info = [[] for _ in range(100001)] # mids

def calc_max_depth(p_id):
    cnt = 1 # min(max_depth - limit)이 0보다 커야함.
    min_value = 100001
    while True:
        if p_id == -1:
            break
        now_max_depth = node_info[p_id][1]
        min_value = min(min_value, now_max_depth - cnt)
        cnt += 1
        p_id = parent_info[p_id]
    if min_value > 0:
        return True
    else:
        return False

def add_node(m_id, p_id, color, max_depth): # 최종 루트 노드까지 parent 노드들을 탐색하며 가능한 maxdepth 계산. min(현재 노드의 maxdepth - cnt) > 0이면 노드 추가 가능
    flag = calc_max_depth(p_id)
    if flag == False: # 노드를 추가할 수 없는 경우
        return
    node_info[m_id][0] = color
    node_info[m_id][1] = max_depth
    parent_info[m_id] = p_id
    child_info[p_id].append(m_id)
    
def change_color(m_id, color): # mid 노드를 루트 노드로 하는 서브트리의 노드 mid 반환
    node_info[m_id][0] = color
    for m_id in child_info[m_id]:
        change_color(m_id, color)
    return


def calc_value(m_id, color_set):
    color_set.add(node_info[m_id][0])
    for child in child_info[m_id]:
        calc_value(child, color_set)

def score(): # 루트 노드부터 시작
    total_score = 0
    for i in range(100001):
        color, max_depth = node_info[i]
        if color == 0 and max_depth == 0:
            continue
        color_set = set()
        calc_value(i, color_set)
        total_score += (len(color_set)) ** 2
    print(total_score)


Q = int(input()) # 명령어 수 입력

for _ in range(Q):
    command = list(input().split())
    cmd_type = command[0]
    if cmd_type == '100': # 노드 추가
        m_id, p_id, color, max_depth = command[1:]
        add_node(int(m_id), int(p_id), int(color), int(max_depth))
    elif cmd_type == '200': # 색깔 변경
        m_id, color = command[1:]
        change_color(int(m_id), int(color))
    elif cmd_type == '300': # 색깔 조회
        m_id = command[1]
        print(node_info[int(m_id)][0])
    elif cmd_type == '400': # 점수 조회
        score()