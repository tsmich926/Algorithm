from collections import deque

def BFS(si, sj):
    global Island
    queue = deque()
    queue.append([si, sj])
    visited[si][sj] = True
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == 1 and not visited[ni][nj]:
                queue.append([ni, nj])
                visited[ni][nj] = True

    Island += 1
    return


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    Island = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 1 and not visited[i][j]:    # 배열을 돌면서 육지이고 방문하지 않았으면 BFS로 그 부분 땅을 전부다 방문했다는 표시를 남긴다
                BFS(i, j)                               # 카드 뒤집는 거라고 생각하고 풀었음
    print(Island)
