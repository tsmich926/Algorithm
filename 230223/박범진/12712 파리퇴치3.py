T = int(input())
#     위 아래 왼 오른
dr_a = [0, -1, 1, 0, 0]
dc_a = [0, 0, 0, -1, 1]
#    왼위 왼아래 오른위 오른아래
dr_b = [0, -1, 1, -1, 1]
dc_b = [0, -1, -1, 1, 1]
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 배열의 크기는 N*N, M은 스프레이의 길이
    ARR = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N):
        for j in range(N):
            sumV = 0
            sumV += ARR[i][j]    # 처음 시작하는 곳을 일단 더하고
            for l in range(1, M):
                for k in range(1, 5):    # 시작하는 곳을 기준으로 위, 아래, 왼, 오른쪽을 더하기
                    newR = i + dr_a[k] * l    # 스프레이의 길이만큼 곱한다.  시작하는 곳을 제외하고 위, 아래, 왼, 오른쪽을 한칸씩 더하고, for문의 M까지의 길이만큼 한칸씩 나아가면서 또 더한다.
                    newC = j + dc_a[k] * l
                    if 0 <= newR < N and 0 <= newC < N:
                        sumV += ARR[newR][newC]
            if sumV > maxV:
                maxV = sumV

    for i in range(N):    # 위와 똑같은 대각선
        for j in range(N):
            sumV2 = 0
            sumV2 += ARR[i][j]
            for l in range(1, M):
                for k in range(1, 5):
                    newR = i + dr_b[k] * l
                    newC = j + dc_b[k] * l
                    if 0 <= newR < N and 0 <= newC < N:
                        sumV2 += ARR[newR][newC]
            if sumV2 > maxV:
                maxV = sumV2

    print(f'#{tc} {maxV}')