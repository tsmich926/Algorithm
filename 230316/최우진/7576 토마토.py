from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx,ny))





M, N = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = deque()

for row in range(N):
    for col in range(M):
        if arr[row][col] == 1:
            queue.append((row, col))

BFS()

ans = 0
for row in range(N):
    for col in range(M):
        if arr[row][col]==0:
            print(-1)
            exit()
        else:
            if arr[row][col]>ans:
                ans = arr[row][col]

print(ans-1)