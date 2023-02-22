def par(k):
    if k == M:                    # 원하는 길이의 수열이 만들어졌다면
        for i in range(M):        # 수열의 길이만큼만 읽음, 그 이후의 비트 자리들은 모두 -1이기 때문에
            idx = bits[i]         # bits의 각 자리에는 인덱스가 들어가있음
            print(lst[idx], end=' ')  # 출력 조건에 맞춰 출력
        print()
        return                    # 끝나면 14행으로 가서 False만든 후 반복문 다시 시작

    for i in range(N):            # 전체 길이만큼 돌려줌, 재귀로 다시 돌려서 k==m이 아니라면 여기로
        if not visited[i]:        # 방문하지 않았다면
            visited[i] = True     # 방문표시
            bits[k] = i           # 방문한 곳 인덱스를 넣어줌
            par(k+1)              # 재귀로 함수 다시 돌림
            visited[i] = False



N, M = map(int, input().split())
lst = list(range(1, N+1))
bits = [-1] * N            # 수열이 될 숫자 넣어줄 리스트
visited = [False] * N      # 방문 여부 표시
par(0)