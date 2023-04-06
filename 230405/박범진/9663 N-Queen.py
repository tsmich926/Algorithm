# def promising(i, j):
#     for di, dj in [[-1, -1], [-1, 0], [-1, 1]]:
#         ni, nj = i + di, j + dj
#         while 0 <= ni < N and 0 <= nj < N:
#             if board[ni][nj]:  # 다른 퀸이 있으면
#                 return 0  # 실패
#             ni, nj = ni + di, nj + dj
#     return 1  # i, j에 퀸을 놓을 수 있음
# 
# 
# def f(i):
#     global cnt
#     if i == N:  # N개의 퀸을 놓은 경우
#         cnt += 1
#     else:
#         for j in range(N):
#             if promising(i, j):
#                 board[i][j] = 1
#                 f(i + 1)
#                 board[i][j] = 0
# 
# 
# N = int(input())
# 
# board = [[0] * N for _ in range(N)]
# cnt = 0
# f(0)
# print(cnt)





def dfs(n):
    global ans
    if n == N:    # N행까지 진행한 경우 가능: 성공
        ans += 1
        return

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:    # 열/대각선 모두 퀸이 없는 경우
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

N = int(input())
ans = 0
v1 = [0]*N             # 같은열 방문 체크용
v2 = [0]*(2*N)         # /방향 방문 체크용
v3 = [0]*(2*N)         # \방향 방문 체크용
dfs(0)
print(ans)