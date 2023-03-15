'''
가로 세로 탐색
가로 N
세로 M
가로 혹은 세로를 반복하면서 1이나오면 카운트
0이 나오면 카운트를 0으로 리셋
가장 긴 구조물의 길이를 출력
'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0
    for i in range(N):                               # 가로 탐색
        cnt = 0
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
                if max_len < cnt and cnt >= 2:        # 구조물의 최소크기가 1X2이기 때문에 가로세로 합치면 최소값이 2
                    max_len = cnt
            else:
                cnt = 0

    for i in range(M):                               # 세로탐색
        cnt = 0
        for j in range(N):
            if board[j][i] == 1:
                cnt += 1
                if max_len < cnt and cnt >= 2:
                    max_len = cnt
            else:
                cnt = 0
    print(f'#{tc} {max_len}')