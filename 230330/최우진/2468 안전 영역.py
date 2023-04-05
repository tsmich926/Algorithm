from collections import deque
import copy

def Q(r,c):
    global farr

    q = deque()
    q.append((r, c))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]
            if nr >= 0 and nr <N and nc >= 0 and nc < N:


                if farr[nr][nc] != 0:

                    q.append((nr, nc))
                    farr[nr][nc] = 0




N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

lis = [1]

maxV = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] >= maxV:
            maxV = arr[i][j]

for i in range(1, maxV):

    farr = copy.deepcopy(arr)

    for row in range(N):
        for col in range(N):
            if farr[row][col] <= i:
                farr[row][col] = 0
    # print(farr)



    cnt = 0
    for r in range(N):
        for c in range(N):
            if farr[r][c] > 0:
                Q(r,c)
                cnt += 1
    lis.append(cnt)
# print(lis)
print(max(lis))