'''
N제곱 부터 1씩 줄어드는 달팽이 모양으로 품
'''


import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
target = int(input())
arr = [[0]*N for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
d = i = j = 0
k = arr[i][j] = N**2    # 처음 N제곱 추가
if k == target:  # 처음 N제곱 값이 타겟일 경우 ( 예외 케이스 )
    ans_i = i + 1
    ans_j = j + 1
while k > 1:
    newR = i + dr[d]
    newC = j + dc[d]
    if newR < 0 or newC < 0 or newR >= N or newC >= N or arr[newR][newC] != 0:
        d = (d+1) % 4
        continue
    else:
        k -= 1
        i, j = newR, newC
        arr[i][j] = k
        if k == target:
            ans_i = i+1
            ans_j = j+1

for row in range(N):
    print(*arr[row])

print(ans_i, ans_j)