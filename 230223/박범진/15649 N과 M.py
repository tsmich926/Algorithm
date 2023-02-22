def per(k):
    if k == M:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            per(k+1)
            visited[i] = False
            ans.pop()

N , M = map(int, input().split())
visited = [False] * (N+1)
ans = []

per(0)