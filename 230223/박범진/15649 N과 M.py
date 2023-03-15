def per(k):
    if k == M:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, N+1):
        if not visited[i]:    # 방문하지 않았던 곳을 방문하고
            visited[i] = True
            ans.append(i)    # ans에 더하기
            per(k+1)    # k를 1씩 늘려가며 계속 호출하다가 원하는 배열의 길이(M)에 도달하면 return
            visited[i] = False    # return 후에는 다시 방문하지 않은것으로 만듬
            ans.pop()    # ans에 더했던 것 빼기

N , M = map(int, input().split())
visited = [False] * (N+1)
ans = []

per(0)