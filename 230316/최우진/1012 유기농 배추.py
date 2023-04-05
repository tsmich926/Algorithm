from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue

            if arr[nx][ny] == 1:
                queue.append((nx,ny))
                arr[nx][ny] = 0
    return


TC = int(input())
for tc in range(TC):
    M, N, K = list(map(int, input().split()))
    arr = [[0]*M for _ in range(N)]

    for i in range(K):
        x, y = list(map(int, input().split()))
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)