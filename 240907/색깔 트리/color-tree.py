# 노드 추가: 노드를 트리에 추가. pid == -1이면 루트 노드
# 색깔 변경: 서브트리의 모든 노드의 색을 변경한다.
# 색깔 조회: 특정 노드의 현재 색깔을 조회한다.
# 점수 조회: 모든 노드의 가치의 제곱의 합을 출력. 가치는 해당 노드를 루트로하는 서브트리의 서로 다른 색의 개수
# color - 1:빨강, 2:주황, 3:노랑, 4:초록, 5:파랑

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

roots = []
node_info = [[0, 0] for _ in range(100001)] # color, maxdepth
parent_info = [0] * 100001 # pid
child_info = [[] for _ in range(100001)] # mids

def calc_max_depth(m_id, p_id, depth):
    min_depth = min(depth, node_info[p_id][1] - 1)
    if min_depth > 0:
        node_info[m_id][1] = min_depth
        return True
    else:
        return False

def add_node(m_id, p_id, color, max_depth): # 최종 루트 노드까지 parent 노드들을 탐색하며 가능한 maxdepth 계산. min(현재 노드의 maxdepth - cnt) > 0이면 노드 추가 가능
    if p_id == -1:
        node_info[m_id][0] = color
        node_info[m_id][1] = max_depth
        parent_info[m_id] = p_id  
    else:  
        flag = calc_max_depth(m_id, p_id, max_depth)
        if flag == False: # 노드를 추가할 수 없는 경우
            return
        node_info[m_id][0] = color
        parent_info[m_id] = p_id
        child_info[p_id].append(m_id)
    
def change_color(m_id, color): # mid 노드를 루트 노드로 하는 서브트리의 노드 mid 반환
    node_info[m_id][0] = color
    for m_id in child_info[m_id]:
        change_color(m_id, color)
    return


def calc_value(m_id):
    global total_score
    child_color_set = set()
    for child in child_info[m_id]:
        child_color_set.update(calc_value(child))
    child_color_set.add(node_info[m_id][0])
    total_score += (len(child_color_set)) ** 2
    return child_color_set


total_score = 0
def score(): # 루트 노드부터 시작
    global total_score
    total_score = 0
    for root in roots:
        color_set = calc_value(root)
    print(total_score)


Q = int(input()) # 명령어 수 입력

for _ in range(Q):
    command = list(input().split())
    cmd_type = command[0]
    if cmd_type == '100': # 노드 추가
        m_id, p_id, color, max_depth = command[1:]
        if p_id == '-1':
            roots.append(int(m_id))
        add_node(int(m_id), int(p_id), int(color), int(max_depth))
    elif cmd_type == '200': # 색깔 변경
        m_id, color = command[1:]
        change_color(int(m_id), int(color))
    elif cmd_type == '300': # 색깔 조회
        m_id = command[1]
        print(node_info[int(m_id)][0])
    elif cmd_type == '400': # 점수 조회
        score()