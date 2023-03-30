from collections import deque

def bfs(si, sj):
    visited = [[False] * W for _ in range(H)]
    queue = deque()
    queue.append((si, sj, 0))                  # count 0부터 시작
    visited[si][sj] = True                     # 방문해주기

    while queue:
        ci, cj, count = queue.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == False and arr[ni][nj] == 'L':
                queue.append((ni, nj, count+1))
                visited[ni][nj] = True

    return count

# bfs용
H, W = map(int, input().split())
arr = [list(map(str, input())) for _ in range(H)]
maxV = 0

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'L':
            tmp = bfs(i, j)
            if tmp > maxV:
                maxV = tmp

print(maxV)