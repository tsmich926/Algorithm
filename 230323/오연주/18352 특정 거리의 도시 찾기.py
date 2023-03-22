from collections import deque
import sys

input = sys.stdin.readline

def dfs(v):
    Q = deque()
    visited = [0] * (N+1)
    nlst = []

    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()
        for w in lst[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                if visited[w] > K+1:
                    return nlst
                if visited[w] == K+1:
                    nlst.append(w)
                Q.append(w)
    return nlst




N, M, K, X = map(int, input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    lst[n1].append(n2)

if len(dfs(X)) == 0:
    print(-1)
else:
    for i in sorted(dfs(X)):
        print(i)