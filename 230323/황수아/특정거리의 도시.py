from collections import deque
import sys
n,m,k,x= map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]

#이어진 도시들의 정보를 입력
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    adj[a].append(b)

# 모든 도시 최단 거리 초기화
distance = [-1]*(n+1)
distance[x]=0
deq=deque([x])
while deq:
    target = deq.popleft()
    for next_node in adj[target]:
        if distance[next_node] == -1:
            distance[next_node] = distance[target] + 1
            deq.append(next_node)

check = True
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = False
# 최단거리가 k인 도시가 존재하지 않을 경우 
if check:
    print(-1)