from collections import deque


def check(board):
    global answer
    global visit
    result = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N - 1):
            if L <= abs(board[i][j] - board[i][j + 1]) <= R:
                result[i][j] = 1
                result[i][j + 1] = 1

    for i in range(N-1):
        for j in range(N):
            if L <= abs(board[i][j] - board[i + 1][j]) <= R:
                result[i][j] = 1
                result[i + 1][j] = 1                                # result를 구함  (result는 국경을 열어야할지 말아야 할지 체크하는 용도)


    for i in result:
        visit += sum(i)                                             # result의 합을 구함

    if visit == 0:                                                  # result원소의 합이 0이면 조건에 맞는 나라가 없다는 뜻이니까 국경을 열지 않음
        return

    for i in range(N):                                              # result원소의 합이 0이 아니면 result배열을 돌면서 방문하지 않은곳을 bfs를 돌기
        for j in range(N):
            if result[i][j] == 1 and not visited[i][j]:
                bfs(0, 0, visited, result)

    answer += 1


def bfs(ci, cj, visited, result):
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]
    queue = deque()
    queue.append([ci, cj])
    sumV = 0
    cntV = 0
    visited[ci][cj] = True        
    sumV += arr[ci][cj]            # 평균을 내기 위한 sumV
    cntV += 1                      # 평균을 내기 위한 cntV
    while queue:
        ci, cj = queue.popleft()
        for i in range(4):
            ni = ci + di[i]
            nj = cj + dj[i]
            if 0 <= ni < N and 0 <= nj < N and result[ni][nj] == 1 and not visited[ni][nj]:    # 상하좌우를 기준으로 result가 1이면 국경이 열려있다는 뜻이고 visited가 False이면 방문하지 않았다는 뜻
                visited[ni][nj] = True
                queue.append([ni, nj])
                sumV += arr[ni][nj]           # 평균을 내기 위한 sumV
                cntV += 1                     # 평균을 내기 위한 cntV

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                arr[i][j] = sumV//cntV        # 방문한 곳의 원소를 전부 평균 값으로 바꿔줌

    return



N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0


visit = 0
check(arr)                   # 처음에 국경을 열어야할지 말아야할지 체크
while visit != 0:            # 그 후에 또 국경을 열어야 할지 말아야할지 계속 체크
    visit = 0
    check(arr)

print(arr)
print(answer)