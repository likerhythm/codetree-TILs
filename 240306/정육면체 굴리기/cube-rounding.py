#칸 == 0 이면 주사위 바닥면 복사.
#칸 != 0 이면 칸 복사, 칸 = 0
#이동할 때마다 정육면체 상단면 출력

n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 상단, 뒷단, 앞단, 좌단, 우단, 하단
dice = [0, 0, 0, 0, 0, 0]

#북쪽으로 이동
#상단 -> 뒷단
#뒷단 -> 하단
#하단 -> 앞단
#앞단 -> 상단
def north(dice):
    dice[1], dice[5], dice[2], dice[0] = dice[0], dice[1], dice[5], dice[2]


#남쪽으로 이동
#상단 -> 앞단
#뒷단 -> 상단
#하단 -> 뒷단
#앞단 -> 하단
def south(dice):
    dice[2], dice[0], dice[1], dice[5] = dice[0], dice[1], dice[5], dice[2]


#동쪽으로 이동
#상단 -> 우단
#좌단 -> 상단
#하단 -> 좌단
#우단 -> 하단
def east(dice):
    dice[4], dice[0], dice[3], dice[5] = dice[0], dice[3], dice[5], dice[4]


#서쪽으로 이동
#상단 -> 좌단
#좌단 -> 하단
#하단 -> 우단
#우단 -> 상단
def west(dice):
    dice[3], dice[5], dice[4], dice[0] = dice[0], dice[3], dice[5], dice[4]


def setDiceAndBoard(board, dice):
    if board[dice_n][dice_m] == 0:
        board[dice_n][dice_m] = dice[5]
    else:
        dice[5] = board[dice_n][dice_m]
        board[dice_n][dice_m] = 0

    #주사위 상단 출력
    print(dice[0])

#1~4 동서북남
step = list(map(int, input().split()))

dice_n = x
dice_m = y

for s in step:
    match s:
        #동
        case 1:
            if dice_m + 1 < m:
                east(dice)
                dice_m += 1
                setDiceAndBoard(board, dice);
        #서
        case 2:
            if dice_m - 1 >= 0:
                west(dice)
                dice_m -= 1
                setDiceAndBoard(board, dice);
        #북
        case 3:
            if dice_n - 1 >= 0:
                north(dice)
                dice_n -= 1
                setDiceAndBoard(board, dice);
        #남
        case 4:
            if dice_n + 1 < n:
                south(dice)
                dice_n += 1
                setDiceAndBoard(board, dice);