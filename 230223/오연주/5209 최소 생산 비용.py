def per(k, curS):          # 함수에 넣어주는 값으로 시작 값, 합
    global minV
    if curS > minV:        # 합이 최소값 넘어가버리면 종료
        return
    if k == N:             # N 길이의 조합 만들었을 시
        if minV > curS:    # 합과 최소값 비교
            minV = curS
        return


    for i in range(N):              # 한 줄에 하나씩만 골라야 하므로
        if not visited[i]:          # 방문하지 않았을 시
            visited[i] = True       # 방문표시
            bits[i] = arr[k][i]     # 비트의 i번째 자리를 줄에 하나씩 고른 값으로 넣어줌
            per(k+1, curS + arr[k][i])    # k+1번째 자리에 넣어줄 다음 함수 실행, 합에 이미 넣은 값 추가
            visited[i] = False



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bits = [-1] * N
    visited = [False] * N
    minV = 1500000
    per(0, 0)
    print(f'#{tc} {minV}')