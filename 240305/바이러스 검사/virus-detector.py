import math

n = int(input())
REST = list(map(int, input().split()))
LDR, MBR = map(int, input().split())

answer = 0
for R in REST:
    answer = answer + 1
    if R-LDR > 0:
        answer =+ math.ceil((R-LDR)/MBR)
print(answer)