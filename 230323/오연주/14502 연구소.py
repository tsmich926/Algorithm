from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

def bfs():
    Q = deque()
    visited = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 2:
                visited[i][j] = 1
                Q.append((i, j))
            if lst[i][j] == 1:
                visited[i][j] = 1

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0<=newR<N and 0<=newC<M and not visited[newR][newC]:
                visited[newR][newC] = 1
                Q.append((newR, newC))

    global res
    cnt = 0
    for i in range(N):
        cnt += visited[i].count(0)
    res = max(cnt, res)




def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 0:
                lst[i][j] = 1
                wall(cnt+1)
                lst[i][j] = 0


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
res = 0
wall(0)
print(res)

