# 1. 재귀 DFS
# G: 그래프, v: 시작정점
# visited: 정점의 방문 정보 표시, False로 초기화
# G[v]: 그래프 G에서 v의 인접 정점 리스트

# def DFS(G, v):
#     visited[v] = True        # 시작 정점v를 방문하고
#     visit(v)                 # 원하는 작업을 수행
#     for w in G[v]:           # 정점v에 인접해있는 모든 정점에 대해서 반복
#         if not visited[w]:   # 인접 정점 w가 방문하지 않은 정점인지 검사하고
#             DFS(G, w)        # 정점 w를 방문하기 위해 재귀 호출


# 2. 스택을 이용한 반복 DFS
# # G: 그래프, v: 시작정점
# # G[v]: 그래프 G에서 v의 인접 정점 딕셔너리
# def DFS(G, v):
#     need_visited = list()                     # 기본은 항상 두개의 리스트를 별도로 관리해주는 것
#     visited = list()                          # !!! from collections import deque 를 써서 deque 패키지를 불러오면 need_visited = deque()로 바꿔 쓸 수 있음(성능이 더 좋음)
#     need_visited.append(v)                    # 시작 노드를 시정하기
#     while need_visited:                       # 만약 아직도 방문이 필요한 노드가 있다면,
#         node = need_visited.pop()             # 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
#         if node not in visited:               # 만약 그 노드가 방문한 목록에 없다면
#             visited.append(node)              # 방문한 목록에 추가하기
#             need_visited.extend(G[node])      # 그 노드에 연결된 노드를
#     return visited


# 3. 큐를 이용한 반복 BFS
# G: 그래프, v: 시작정점
# G[v]: 그래프 G에서 v의 인접 정점 리스트
# from collections import deque    # 큐 구현을 위해 deque라이브러리 사용

# def BFS(G, v, visited):
#     queue = deque([v])
#     visited[v] = True            # 현재 노드 방문 처리
#     while queue:                 # 큐가 빌 때까지 반복
#         x = queue.popleft()      # 큐에서 하나의 원소를 뽑아 출력
#         print(v, end=' ')
#         for i in G[x]:           # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True


from collections import deque

res = []
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for node in Graph[x]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


for m in range(int(input())):
    tmp = 0
    N, M = map(int, input().split())
    Graph = [[] for i in range(N + 1)]
    visited = [False] * (N + 1)
    for i in range(M):
        A, B = map(int, input().split())
        Graph[A].append(B)
        Graph[B].append(A)

    for i in range(1, N + 1):
        if not visited[i]:
            BFS(i)
            tmp += 1
    res.append(tmp)
for i in range(len(res)):
    print("#%d %s" % (i + 1, res[i]))