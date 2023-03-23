'''
board를 만들고
bfs혹은 dfs로 1을 찾아서 방문표시를 해주며 지워간다
그 그룹에서 전부 지우면 ans+= 1
최종적으로 ans(지렁이의 수) 를 출력
'''

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(x,y):
    q = deque([])
    q.append([x,y])
    arr[x][y] = 0
    while q:
        r, c = q.popleft()
        for d in range(4):
            newR = r + dr[d]
            newC = c + dc[d]
            if 0 <= newR < N and 0 <= newC < M and arr[newR][newC] == 1:
                q.append([newR,newC])
                arr[newR][newC] = 0

T = int(input())

for tc in range(1,T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]


    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:           # bfs 재귀 형태로 풀이
                bfs(i,j)                 # 그룹핑된 1값들을 전부 0으로 만들어주고
                ans += 1                 # ans ( 지렁이의수 ) 를 증가시킴
    print(ans)
