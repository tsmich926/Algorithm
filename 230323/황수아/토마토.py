from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] #위아래양옆
res = 0

#익은 토마토의 위치파악
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft() #토마토 좌표꺼내기
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0: #유효범위검사하고 토마토가 안익었는지 검사
                matrix[nx][ny] = matrix[x][y] + 1 #익히고 1더해주기
                queue.append([nx, ny])

bfs()
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)