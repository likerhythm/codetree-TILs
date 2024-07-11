n = int(input())

arr = []
temp = []
arr_size = n
temp_size = 0
for _ in range(n):
    arr.append(int(input()))

def remove_block(array, s, e):
    temp = []
    for i in range(len(array)):
        if s <= i <= e:
            continue
        temp.append(array[i])
    return temp

for _ in range(2):
    s, e = map(int, input().split())
    arr = remove_block(arr, s - 1, e - 1)

print(len(arr))
for a in arr:
    print(a)