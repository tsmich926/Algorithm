# 사이클이 생기지 않도록 간선 포함 여부를 확인-find
#합쳐서 네트워크를 형성-union
# 두 간선의 부모가 다를때 합치기 가능
# 부모가 같으면 사이클을 형성하여  mst의 조건에 부합하지 않음

# -도시들을 mst로 연결
# -mst로 연결했을때 간선들 합의 최솟값 구하기
# -간선 최솟합에 세율곱하기



#heappush
#heappop heap에서 가장 작은 원소를 pop

# 특정 원소가 속한 집합을 찾기
# def find_parent(parent, x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         return find_parent(parent, parent[x])
#     return x

# # 두 원소가 속한 집합을 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


# def dis_calc(x, y):
#     i1 = xs[x]
#     i2 = xs[y]

#     j1 = ys[x]
#     j2 = ys[y]
#     return (i1 - i2) ** 2 + (j1 - j2) ** 2

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     islands = [[0] * N for _ in range(N)]
#     cost = [0] * N
#     xs = list(map(int, input().split()))
#     ys = list(map(int, input().split()))
#     E = float(input())



import heapq

T =int(input())
for tc in range(1, T+1):
    n = int(input())
    x_location = list(map(int, input().split()))
    y_location = list(map(int, input().split()))
    tax = float(input())

    # 인접 리스트
    adj = {i: [] for i in range(n)}
    for s in range(n):
        for e in range(n):
            if s != e:
                adj[s].append([e, (x_location[s]-x_location[e])**2 + (y_location[s]-y_location[e])**2]) #시작점,간선 넣기

    # Key: 가장 큰 값들로 채운다 / 이후 최소 가중치들을 채움
    # mst: visit
    key = [float('inf')] * n
    mst = [False] * n
    pq = []

    # 시작
    # 시작점 가중치
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0

    while pq:
        # 가중치가 최소인 정점을 뽑는다.
        k, u = heapq.heappop(pq)

        # 이미 방문한 적이 있으면 건너뜀
        if mst[u]:
            continue

        # 아니라면 방문표시와 가중치를 결과에 더해준다.
        mst[u] = True
        result += k

        # dest: 정점 u에서 갈수 있는 곳
        # w: u -> dest 의 가중치
        for dest, w in adj[u]:
            # 그 중 방문한 적이 없고 현재까지 방문했던 가중치보다 작다면
            if not mst[dest] and w < key[dest]:
                # 새로 갱신해준다.
                key[dest] = w
                heapq.heappush(pq, (w, dest))

    print('#{} {}'.format(tc, round(result*tax))) 