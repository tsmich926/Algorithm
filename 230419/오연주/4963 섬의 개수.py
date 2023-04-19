from collections import deque

dr = [0, 0, 1, -1, -1, 1, -1, 1]
dc = [1, -1, 0, 0, -1, 1, 1, -1]

def bfs(row, col):
    Q = deque()
    Q.append((row, col))
    visited[row][col] = 1

    while Q:
        r, c = Q.popleft()
        for i in range(8):
            newR = r + dr[i]
            newC = c + dc[i]
            if 0<=newR<h and 0<=newC<w and not visited[newR][newC]:
                visited[newR][newC] = 1
                Q.append((newR, newC))




while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    lst = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if lst[i][j] == 0:
                visited[i][j] = 1
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)