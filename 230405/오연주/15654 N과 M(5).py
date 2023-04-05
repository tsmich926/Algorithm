def check(k):
    if k == M:
        print(*result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(lst[i])
            check(k+1)
            visited[i] = 0
            result.pop()



N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [0]*N
result = []
check(0)