# 시간어떻게줄일거?

import sys

input = sys.stdin.readline

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def bfs(lst):
    global minV
    visited = [[100] * N for _ in range(N)]
    if not lst:
        return

    for i in lst:
        row, col = i
        for j in homelst:
            row2, col2 = j
            visited[row2][col2] = min(visited[row2][col2], abs(row - row2) + abs(col - col2))
    sumV = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 100:
                sumV += visited[i][j]

    if sumV < minV:
        minV = sumV


def par(k):
    if k == N:
        lst = []
        if result.count(1) <= M:
            for i in range(N):
                if result[i] == 1:
                    lst.append(shoplst[i])
        bfs(lst)
        return
    result[k] = 1
    par(k + 1)
    result[k] = 0
    par(k + 1)


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
shoplst = []
homelst = []
minV = 100 * 2500


for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            shoplst.append((i, j))

        if lst[i][j] == 1:
            homelst.append((i, j))
le = len(shoplst)
result = [-1] * le
par(0)
print(minV)