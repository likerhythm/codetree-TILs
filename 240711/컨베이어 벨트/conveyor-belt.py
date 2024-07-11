n, t = map(int, input().split())

arr = []

arr.extend(list(map(int, input().split())))
arr.extend(list(map(int, input().split())))

for _ in range(t):
    temp = arr[2 * n - 1]
    for i in range(2 * n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = temp


for i in range(2 * n):
    if n == i:
        print()
    print(arr[i], end=' ')