from collections import deque



    # 상 우 하 좌
r = [-1, 0, 1, 0]
c = [0, 1, 0, -1]
def bfs(x, y, K):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+c[i], y+r[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and arr[nx][ny] > K:
                queue.append((nx, ny))
                visited[nx][ny] = True

# bfs자체는 전형적인 델타를 이용해서 갈 수 있는 범위만큼 visited를 True로 바꿔주는 bfs


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0


# 1. 물에 잠기는 영역을 전부 검사해 봐야함
# 2. 배열에서 최소값보다 작으면 하나도 안잠기고 최대값보다 크면 모두 잠기기 때문에 범위를 정해줘야함
# 3. 그리고 난 후에 bfs로 검사

max_num = 0
min_num = 101
for i in arr:                             #
    if max(i) > max_num:
        max_num = max(i)
    if min(i) < min_num:
        min_num = min(i)


for K in range(min_num, max_num):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):                                     # 배열을 전부 한칸씩 조건에 맞는지 확인하고 맞으면 bfs를 돌린다.
        for j in range(N):
            if visited[i][j] == False and arr[i][j] > K:
                bfs(i, j, K)                               # bfs를 돌려서 조건에 맞는(물의 높이보다 위에 있는) 지역들을 전부 visited처리를 해주고,
                count += 1                                 # 더이상 나아 갈 수 없으면 count를 1을 더해주고 다시 for문의 다음영역부터 조건을 검사한다.
    answer = max(answer, count)                            # 마지막으로 최대값을 갱신해주면서 K가 몇일때 최대인지 찾으면 끝!

print(answer)
