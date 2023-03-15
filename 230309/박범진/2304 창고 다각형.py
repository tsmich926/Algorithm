import sys

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
arr.sort()


max_height = 0

for value in range(N):                 # 가장 긴 기둥의 길이를 구하기
    if arr[value][1] > max_height:
        max_height = arr[value][1]

left = 0
left_value = 0
for lv in range(N):
    if arr[lv][1] == max_height:
        left = arr[lv][0]              # 왼쪽을 기준으로 가장 긴 기둥의 좌표
        left_value = lv                # 왼쪽에서 가장 긴 기둥의 인덱스 번호
        break

right = 0
right_value = 0
for rv in range(N-1, -1, -1):
    if arr[rv][1] == max_height:
        right = arr[rv][0]              # 오른쪽을 기준으로 가장 긴 기둥의 좌표
        right_value = rv                # 오른쪽에서 가장 긴 기둥의 인덱스 번호
        break


sumV = 0

height = arr[0][1]
for i in range(0, left_value):           # 가장 긴 기둥까지 왼쪽의 블럭을 다 더하기
    if height <= arr[i][1]:
        height = arr[i][1]
        sumV += height*(arr[i+1][0] - arr[i][0])
    else:
        sumV += height*(arr[i+1][0] - arr[i][0])


height = arr[N-1][1]
for i in range(N-1, right_value, -1):    # 가장 긴 기둥까지 오른쪽의 블럭을 다 더하기
    if arr[i][1] <= height:
        sumV += height*((arr[i][0]+1) - (arr[i-1][0]+1))
    elif arr[i][1] > height:
        height = arr[i][1]
        sumV += height*((arr[i][0]+1) - (arr[i-1][0]+1))


sumV += max_height*(right-left+1)         # 가장 긴 기둥의 블럭을 다 더하기
print(sumV)