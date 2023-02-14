T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    # 가로 확인
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:  # 1이 나올 경우
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:     # 0일 경우
                cnt = 0

    # 세로 확인
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0

    print(f'#{tc} {maxV}')