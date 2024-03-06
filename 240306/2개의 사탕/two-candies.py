from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
rn, rm, bn, bm = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rn, rm = i, j
        elif board[i][j] == 'B':
            bn, bm = i, j
board[rn][rm] = '.'
board[bn][bm] = '.'

#시계방향
move_n = [-1, 0, 1, 0]
move_m = [0, 1, 0, -1]

answer = -1
queue = deque([(rn, rm, bn, bm, 0)])
visited = [[rn, rm, bn, bm]]

while queue:
    t_rn, t_rm, t_bn, t_bm, cnt = queue.popleft()
    for i in range(4):
        if cnt > 10:
            print(-1)
            exit(0)
        #파란 사탕 굴리기
        next_bn = t_bn
        next_bm = t_bm
        while board[next_bn + move_n[i]][next_bm + move_m[i]] == '.':
            next_bn += move_n[i]
            next_bm += move_m[i]
        #파란 사탕이 구멍에 빠진 경우 다음 케이스로 이동
        if board[next_bn + move_n[i]][next_bm + move_m[i]] == 'O':
            continue
        #빨간 사탕 굴리기
        next_rn = t_rn
        next_rm = t_rm
        while board[next_rn + move_n[i]][next_rm + move_m[i]] == '.':
            next_rn += move_n[i]
            next_rm += move_m[i]
        #빨간 사탕이 구멍에 빠진 경우 종료
        if board[next_rn + move_n[i]][next_rm + move_m[i]] == 'O':
            print(cnt + 1)
            exit(0)
        #두 사탕이 같은 위치인 경우
        if next_rn == next_bn and next_rm == next_bm:
            if abs(t_rn - next_rn) + abs(t_rm - next_rm) > abs(t_bn - next_bn) + abs(t_bm - next_bm):
                next_rn -= move_n[i]
                next_rm -= move_m[i]
            else:
                next_bn -= move_n[i]
                next_bm -= move_m[i]
        if [next_rn, next_rm, next_bn, next_bm] not in visited:
            queue.append((next_rn, next_rm, next_bn, next_bm, cnt + 1))
            visited.append([next_rn, next_rm, next_bn, next_bm])