import math

n = int(input())
REST = list(map(int, input().split()))
LDR, MBR = map(int, input().split())

answer = 0
for R in REST:
    answer =+ 1
    if R-LDR > 0:
        print(math.ceil((R-LDR)/MBR))
        answer =+ math.ceil((R-LDR)/MBR)
print(answer)