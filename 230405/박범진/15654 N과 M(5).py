def dfs(node):
    if node == M:
        print(*result)
        return

    else:
        for i in range(N):
            if visited[i] == False:
                result[node] = lst[i]
                visited[i] = True
                dfs(node+1)
                visited[i] = False



N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * N
result = [0] * M
dfs(0)