T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mmax = 0 
    #가로 검사
    for row in range(N):
        for col in range(M):
            cnt = 0 #열이 바뀔때마다 cnt갯수는 초기화
            if arr[row][col] == 1:
                if mmax < cnt:
                    mmax = cnt
            else:
                cnt = 0
    #세로검사
    for col in range(M):
        cnt = 0 #행이 바뀔때마다 초기화
        for row in range(N):
            if arr[row][col] == 1:
                cnt += 1
                if mmax < cnt:
                    mmax = cnt
            else:
                cnt = 0
    print(f'#{tc} {mmax}')
    
