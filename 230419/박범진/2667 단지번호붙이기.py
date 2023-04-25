from collections import deque

def BFS(si, sj):
    global area
    queue = deque()
    queue.append([si, sj])
    visited[si][sj] = True
    ans = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1 and not visited[ni][nj]:
                queue.append([ni, nj])
                visited[ni][nj] = True
                ans += 1

    area += 1
    return ans


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
area = 0
count = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:    # 섬의 개수 문제와 마찬가지로 배열을 돌면서 1인곳과 방문하지 않은 곳을 BFS로 방문했다는 표시를 남김
            count.append(BFS(i, j))                 # 다른점은 BFS를 다돌고 총 갯수의 합을 정답 배열에 저장해주고 마지막에 오름차순으로 출력
print(area)
count.sort()
for k in count:
    print(k)