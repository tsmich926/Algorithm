# 무한루프...

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def solve(r, c, d):
    global maxV

    if d > 3:
        return

    if d==3 and visited[r][c] == 2:
        if maxV < len(nlst):
            maxV = len(nlst)
        return

    # if lst[r][c] in nlst[:len(nlst)]:
    #     return


    nr, nc = r+dr[d], c+dc[d]
    if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
        visited[nr][nc] = 1
        nlst.append(lst[nr][nc])
        solve(nr, nc, d)
        visited[nr][nc] = 0

    if 0<=d+1<=3 and 0<=d+1<=3:
        nr, nc = r+dr[d+1], c+dc[d+1]
        if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            nlst.append(lst[nr][nc])
            solve(nr, nc, d+1)
            visited[nr][nc] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    visited = [[0] * N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            nlst = [lst[i][j]]
            visited[i][j] = 2
            solve(i, j, 0)
            visited[i][j] = 0
    print(maxV)