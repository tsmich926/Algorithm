def dfs(row, col):
    visited = [[0]*M for _ in range(N)]
    Q = []

    Q.append((row, col))
    visited[row][col] = 1

    while Q:
        row, col = Q.pop(0)
        lst[row][col] = 0
        visited[row][col] = 1
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            newR = row + dr
            newC = col + dc
            if 0<=newR<N and 0<=newC<M and lst[newR][newC] == 1 and not visited[newR][newC]:
                visited[newR][newC] = visited[row][col] + 1
                lst[newR][newC] = 0
                Q.append((newR, newC))
    return



T = int(input())
for i in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    lst = [[0]*M for _ in range(N)]


    for i in range(K):
        x, y = map(int, input().split())
        lst[y][x] = 1

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)