import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N, M, K, X = map(int, input().split())

arr = [[] for _ in range(N+1)]
ans = [-1]*(N+1)
ans[X] = 0

for _ in range(M):
    s, e = list(map(int, input().split()))
    arr[s].append(e)

q = deque([X])
while q:
    cur = q.popleft()
    for w in arr[cur]:
        if ans[w] == -1:
            ans[w] = ans[cur] + 1
            q.append(w)
for i in range(N+1):
    if ans[i] == K:
        print(i)
if K not in ans:
    print(-1)