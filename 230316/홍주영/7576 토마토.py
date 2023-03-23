'''
토마토 문제
익지않은 토마토 : 0
익은 토마토: 1
토마토가 없는 자리 : -1
BFS 문제
1을 찾아서 1부터 출발.
0을 1로 바꿔주고 ans += 1
현 위치에서 갈 수 있는 0이 없으면 끝

끝낸 후 arr 에서 0이 있으면 -1출력
(arr 돌면서 0이 -1에 둘러싸여있으면 -1출력)
'''

import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(x,y):
    q = deque()
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:         # 1 이 여러개 들어 있는 경우 모두 q에 넣어줌
                q.append([i,j])

    while q:
        r, c = q.popleft()
        for d in range(4):
            newR = r + dr[d]
            newC = c + dc[d]
            if 0 <= newR < N and 0 <= newC < M and box[newR][newC] == 0:
                box[newR][newC] = box[r][c] + 1     # 1씩 더해가준다
                q.append([newR, newC])

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

bfs(0, 0)
ans = 0
for row in box:         # 수행이 모두 끝난 후에 박스를 돌면서 0이 있으면
    if 0 in row:        # 예외케이스
        ans = 0
        break
    ans = max(ans, max(row))
print(ans -1)     # -1 해주는 이유는 처음 1인값부터 시작하기 때문문

# 토마토가 하나 이상 있는 경우만 입력으로 주어지기 때문에 box 가 모두 -1인 경우는 제외
