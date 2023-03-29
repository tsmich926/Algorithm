from collections import deque
import sys
input = sys.stdin.readline


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(row, col):
    Q = deque()
    Q.append((row, col))
    while Q:
        r, c = Q.popleft()
        for i in range(4):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0<=newR<N and 0<=newC<N and visited[newR][newC] == 0:
                visited[newR][newC] = visited[r][c]
                Q.append((newR, newC))


# visited 채우는 함수
def check():
    global visited
    safeZ = 0
    for p in range(maxV+1):
        for i in range(N):
            for j in range(N):
                if lst[i][j] < p:
                    visited[i][j] = -1

        cnt = 1
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    visited[i][j] = cnt
                    bfs(i, j)
                    cnt += 1
        safeZ = max(cnt, safeZ)
        visited = [[0] * N for _ in range(N)]
    return safeZ




N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]


# 최대값구하기
maxV = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] > maxV:
            maxV = lst[i][j]
print(check()-1)


