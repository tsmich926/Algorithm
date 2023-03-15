from collections import deque

def bfs():
    v = [[0] * M for _ in range(N)]

    while Q:
        r, c = Q.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newR = r + dr
            newC = c + dc
            if 0<=newR<N and 0<=newC<M and lst[newR][newC] == 0 and v[newR][newC] == 0:
                v[newR][newC] = v[r][c] + 1
                Q.append((newR, newC))

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                visited[i][j] = v[i][j]
            else:
                if visited[i][j] > v[i][j]:
                    visited[i][j] = v[i][j]
    return



M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            Q.append((i, j))
            visited[i][j] = -1
        elif lst[i][j] == -1:
            visited[i][j] = -1
bfs()


maxV = -1
for i in visited:
    if max(i) > maxV:
        maxV = max(i)
    if 0 in i:
        maxV = 0
        break


if maxV == -1:
    print(0)
elif maxV == 0:
    print(-1)
else:
    print(maxV)