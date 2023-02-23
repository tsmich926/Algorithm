# def per(k):
#     if k == M:    # 배열의 길이를 확인
#         print(' '.join(map(str, ans)))    # 1 2 3 이런 상태로 출력하기 위해
#         return
#
#     for i in range(1, N+1):    # 1 ~ N 까지
#         if not visited[i]:    # 중복확인
#             visited[i] = True
#             ans.append(i)    # 배열 추가
#             per(k+1)    # 재귀
#             visited[i] = False    # return으로 돌아오면 실행되게
#             ans.pop()
#
# N , M = map(int, input().split())
# visited = [False] * (N+1)
# ans = []
#
# per(0)


def per(k):
    global maxV, SumV

    if k == N:
        if maxV > SumV:
            maxV = SumV
        return

    if maxV <= SumV:
        return

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            SumV += lst[k][i]
            per(k+1)
            visited[i] = False
            SumV -= lst[k][i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    SumV = 0
    maxV = 99999999

    per(0)
    print(f'#{tc} {maxV}')