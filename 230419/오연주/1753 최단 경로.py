import heapq

def dijk():
    U = [0]*V
    U[K] = 1

    for i in range(V):
        D[i] = G[K][i]

    N = V
    for _ in range(N-1):
        minV = float('inf')
        w = 0
        for i in range(V):
            if U[i] == 0 and minV > D[i]:
                w = i
                minV = D[i]
        U[w] = 1

        for v in range(V):
            if 0<G[w][v]<float('inf'):
                D[v] = min(D[v], D[w]+G[w][v])

    return D


V, E = map(int, input().split())
K = int(input())
V += 1
G = [[float('inf')]*V for _ in range(V)]

for i in range(V):
    G[i][i] = 0

for _ in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w

D = [0]*V

lst = dijk()

for i in lst[1:]:
    if i == float('inf'):
        print('INF')
    else:
        print(i)