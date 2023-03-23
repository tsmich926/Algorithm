import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())

dr = [1, 2, 2, 1, -1, -2, -2, -1]  # 나이트가 이동할 수 있는 델타
dc = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(x, y):
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        r, c = q.popleft()

        if [r, c] == end:      # 시작점이 도착점이면 0리턴
            return 0

        for d in range(8):
            newR = r + dr[d]
            newC = c + dc[d]

            if newR < 0 or newR >= N or newC < 0 or newC >= N:
                continue

            if [newR, newC] == end:
                visited[newR][newC] = True
                return arr[r][c] + 1

            if visited[newR][newC] == False:
                q.append([newR, newC])
                visited[newR][newC] = True        # 1씩 더해주면서 시행횟수 계싼
                arr[newR][newC] = arr[r][c] + 1

for tc in range(1, T+1):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    arr = [[0]*N for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    q = deque()

    x, y = start[0], start[1]
    ans = bfs(x, y)
    print(ans)