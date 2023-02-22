import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2*(M-1))]*(M-1) +[[0]*(M-1) + list(map(int, input().split())) + [0]*(M-1) for _ in range(N)] + [[0]*(N+2*(M-1))]*(M-1)        # 2차원배열을 파리퇴치의 조건에 맞춰서 패딩해줌
    dr = [0, 1, 1, 1, 0, -1, -1, -1]  # 오른쪽부터
    dc = [1, 1, 0, -1, -1, -1, 0, 1]
    d = resS = resD = 0                # d : dr, dc 인덱스로 접근해서 방향을 바꿔줄 값
    for i in range(M-1, N+M-1):
        for j in range(M-1, N+M-1):
            sumDiagonal = arr[i][j]
            sumStraight = arr[i][j]
            for d in range(8):
                for n in range(1, M):
                    newR = i + dr[d] * n
                    newC = j + dc[d] * n
                    if d % 2:                             # 대각선일때
                        sumDiagonal += arr[newR][newC]
                    else:                                 # 가로세로일때
                        sumStraight += arr[newR][newC]
            if resS < sumStraight:
                resS = sumStraight
            if resD < sumDiagonal:
                resD = sumDiagonal
    if resD > resS:                # 대각선의 합이 크면
        print(f'#{tc} {resD}')
    else:                          # 가로세로의 합이 크면
        print(f'#{tc} {resS}')
