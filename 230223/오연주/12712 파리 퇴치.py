dr = [0, 1, 0, -1, 1, 1, -1, -1]     # 8방향 모두 다 확인해야 하므로 앞 4개 : 상하좌우 뒤 4개 : 대각선
dc = [1, 0, -1, 0, 1, -1, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0 
    for i in range(N):
        for j in range(N):
            tempV = lst[i][j]     # 상하좌우 더해줄 곳, 가운데 출발점은 기본값으로 넣어줌
            tempV2 = lst[i][j]    # 대각선 더해줄 곳
            for p in range(4):    # 앞의 네 방향으로
                for k in range(1, M):    # 스프레이의 최대값만큼, 0부터 시작하면 가운데 값이 네번 더해져서 1부터
                    newR = i + dr[p] * k
                    newC = j + dc[p] * k
                    if 0 <= newR < N and 0 <= newC < N:   # 범위 맞춰서
                        tempV += lst[newR][newC]

            for p in range(4, 8):    # 뒤의 네 방향으로
                for k in range(1, M):
                    newR = i + dr[p] * k
                    newC = j + dc[p] * k
                    if 0 <= newR < N and 0 <= newC < N:
                        tempV2 += lst[newR][newC]

            if maxV < tempV:      # 최대값 구해주기
                maxV = tempV

            if maxV < tempV2:
                maxV = tempV2

    print(f'#{tc} {maxV}')
