import sys
sys.stdin = open('input.txt', 'r')

direc = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(x,y, val, rotate):
    global cnt, i, j

    if rotate == 3 and x == i and y == j and len(val) > 2:
        cnt = max(cnt, len(val))
        return

    if 0 <= x < N and 0 <= y < N and cafe[x][y] not in val:
        newV = val + [cafe[x][y]]

        newX = x+direc[rotate][0]
        newY = y+direc[rotate][1]
        dfs(newX, newY, newV, rotate)

        if rotate < 3:
            newX = x+direc[rotate+1][0]
            newY = y+direc[rotate+1][1]
            dfs(newX, newY, newV, rotate+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    cnt = -1
    for i in range(N-1):
        for j in range(1, N-1):
            dfs(i, j, [], 0)

    print(f'#{tc}', cnt)
