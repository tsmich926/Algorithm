# def per(k):
#     if k == M:    # 배열의 길이를 확인
#         print(' '.join(map(str, ans)))
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



# 부분집합을 만드는 문제
# 만들고 난 후에 안의 값들을 더해서 비교해야 한다는 것이 포인트!
def per(k):
    global maxV, SumV    # maxV 와 sumV의 값을 global로 함수내에서 수정

    if k == N:    # 부분집합의 크기, N이 3이면 k가 3이 될때 까지 lst에 3번 추가해야 할테니 크기가 됨
        if maxV > SumV:
            maxV = SumV
        return

    if maxV <= SumV:    # 최소금액을 찾고 있는데 이미 최소금액을 넘어가버리면 의미가 없으므로 return
        return

    for i in range(N):
        if visited[i] == False:    # 방문했다는 표시를 남기고
            visited[i] = True
            SumV += lst[k][i]    # 처음 배열의 값을 sumV에 더하고 그 뒤에 이어질 값들을 재귀호출을 통해서 계속 더함, k가 N이 되면 그때서야 멈추고 비교를 시작
            per(k+1)
            visited[i] = False    # 다 돌고난 후에는 방문했다는 표시를 지우고
            SumV -= lst[k][i]    # sumV도 다시 0으로 만든다


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    SumV = 0
    maxV = 99999999

    per(0)
    print(f'#{tc} {maxV}')
