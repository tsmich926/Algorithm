def dfs(num):
    road = []
    ST = []
    visited = [False] * (N+1)

    ST.append(num)
    visited[num] = True

    while ST:
        v = ST.pop()
        road.append(v)
        for w in lst[v]:
            if not visited[w]:
                visited[w] = True
                ST.append(w)
    return sorted(road)




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst =[[] for _ in range(N+1)]
    flst = []
    for _ in range(M):
        n1, n2 = map(int, input().split())
        lst[n1].append(n2)
        lst[n2].append(n1)
    for i in range(1, N+1):
        v = dfs(i)
        if v not in flst:
            flst.append(v)
    print(f'#{tc} {len(flst)}')