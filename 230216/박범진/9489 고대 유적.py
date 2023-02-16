T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())     # N = 세로(행) M = 가로(열)
    ARR = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0    # 가장 긴 구조물의 길이

    for i in range(N):    # 먼저 가로를 보면서 연속되는 1을 찾기
        count = 0
        for j in range(M):
            if ARR[i][j] == 1:    # 1이 연속되면 0이 나올때까지 더하기
                count += 1
                if max_count < count:    # 가장 긴 구조물과 비교하기
                    max_count = count
            else:                 # 0이 나오면 다시 count초기화
                count = 0

    New_ARR = list(zip(*ARR))    # 가로와 세로를 뒤바꾸는 배열을 새로 만든다

    for i in range(M):    # 그리고 위와 똑같이 실행하면 세로도 찾을 수 있음!
        count = 0
        for j in range(N):
            if New_ARR[i][j] == 1:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                count = 0

    print(f'#{tc} {max_count}')