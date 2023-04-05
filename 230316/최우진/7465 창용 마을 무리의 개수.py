from collections import deque


def bfs(s):
    Q = deque()
    Q.append(s)
    visited[s] = True
    while Q:
        v = Q.popleft()
        for w in adjL[v]:
            if visited[w] == False:
                Q.append(w)
                visited[w] = True


TC = int(input())
for tc in range(1, TC + 1):

    N, M = list(map(int, input().split()))
    adjL = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for i in range(M):
        n1, n2 = list(map(int, input().split()))
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == False:
            bfs(i)
            cnt += 1

    print(f'#{tc} {cnt}')