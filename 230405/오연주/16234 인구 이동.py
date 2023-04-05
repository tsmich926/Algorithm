def bfs(row, col):
    tmpidx = [(row, col)]
    tmpnum = lst[row][col]
    Q = []
    Q.append((row, col))
    visited[row][col] = 1

    while Q:
        row, col = Q.pop(0)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR = row + dr
            newC = col + dc
            if 0<=newR<N and 0<=newC<N and not visited[newR][newC]:
                if L<=abs(lst[row][col]-lst[newR][newC])<=R:
                    tmpidx.append((newR,newC))
                    Q.append((newR, newC))
                    visited[newR][newC] = 1
                    tmpnum += lst[newR][newC]

    res = tmpnum // len(tmpidx)
    for r, c in tmpidx:
        lst[r][c] = res

    return len(tmpidx)




N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    result += 1

print(result)