from collections import deque
import sys
input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def bfs(row, col):
    global maxV
    Q = deque()
    visited2 = [[0] * M for _ in range(N)]

    Q.append((row, col))
    visited2[row][col] = 1

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0<=newR<N and 0<=newC<M and visited[newR][newC] == 0 and visited2[newR][newC] == 0:
                visited2[newR][newC] = visited2[r][c] + 1
                Q.append((newR, newC))
                if visited2[newR][newC] > maxV:
                    maxV = max(maxV, visited2[newR][newC])


N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
maxV = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'W':
            visited[i][j] = -1

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            bfs(i, j)

print(maxV-1)
