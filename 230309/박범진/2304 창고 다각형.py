import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
arr.sort()


max_height = 0

for value in range(N):
    if arr[value][1] > max_height:
        max_height = arr[value][1]

left = 0
left_value = 0
for lv in range(N):
    if arr[lv][1] == max_height:
        left = arr[lv][0]
        left_value = lv
        break

right = 0
right_value = 0
for rv in range(N-1, -1, -1):
    if arr[rv][1] == max_height:
        right = arr[rv][0]
        right_value = rv
        break

sumV = 0
height = arr[0][1]

for i in range(0, left_value):
    if height <= arr[i][1]:
        height = arr[i][1]
        sumV += height*(arr[i+1][0] - arr[i][0])
    else:
        sumV += height*(arr[i+1][0] - arr[i][0])

height = arr[N-1][1]

for i in range(N-1, right_value, -1):
    if arr[i][1] <= height:
        sumV += height*((arr[i][0]+1) - (arr[i-1][0]+1))
    elif arr[i][1] > height:
        height = arr[i][1]
        sumV += height*((arr[i][0]+1) - (arr[i-1][0]+1))


sumV += max_height*(right-left+1)
print(sumV)