#기존 파리퇴치와 다른점 : 세기가 주어져서 각 방향으로 퍼져가는 방식으로 파리의 개체수의 합을 구해야 함
#상좌하우 그리고 대각선 나눠서 파리 개체수의 합 구함

TC = int(input())
for tc in range(1, TC+1):

    N, M = list(map(int, input().split()))
     
    arr = [list(map(int, input().split())) for _ in range(N)]
    #1. 상좌하우
    dr1 = [-1,0,1,0]  # 델타 배열 이용 (상하좌우)
    dc1 = [0,-1,0,1]
     
     
     
    lis = []  
    for row in range(N):
        for col in range(N):  # 각 기준점마다
            cnt = arr[row][col] # 기준점의 파리 개체수를 cnt에 넣어주고
     
            for i in range(4): #위에서 만든 델타 배열의 인덱스를 통해서
                if i == 0: #방향이 상 일때
                    for j in range(M-1): #(세기-1) 만큼 반복을 해줄 것인데, j는 뻗어나가는 칸의 개수를 의미
                        newR = row + (dr1[i]-j) #위로 뻗어나가기 때문에 기존의 행에서 j만큼 빼나감
                        if newR>=0 and newR<N: # 새로운 행이 범위 안에 있을 떄
                            cnt += arr[newR][col] # 상으로 이동된 방향에 있는 파리 개체수를 변수 cnt에 더해나감 
                if i == 1: #방향이 좌 일때
                    for j in range(M-1): #(세기-1) 만큼 반복
                        newC = col + (dc1[i]-j) #좌로 뻗어나가기 때문에 기존의 열에서 j만큼 빼나감
                        if newC>=0 and newC<N: # 새로운 열이 범위 안에 있을 때
                            cnt += arr[row][newC] # 좌로 이동된 방향에 있는 파리 개체수를 변수 cnt 더해나감
                if i == 2: #방향이 하 일떄
                    for j in range(M-1):    #위와 같은 방식으로 방향대로 더해감, 하 일때와 우 일때는 기존의 행과 열에서 j만큼 더해주는 방식으로 개체수의 합 구해줌
                        newR = row + (dr1[i]+j)
                        if newR >= 0 and newR < N:
                            cnt += arr[newR][col]
                if i == 3: #방향이 우 일때
                    for j in range(M-1):
                        newC = col + (dc1[i]+j)
                        if newC >= 0 and newC < N:
                            cnt += arr[row][newC]
            lis.append(cnt)
     
     
     
    #2.대각선 파리의 개체수 합
    dr2 = [-1, 1, 1, -1]  # 델타 배열 이용 (대각선)
    dc2 = [-1,-1,1,1]
     
    lis2 = []
    for row2 in range(N):
        for col2 in range(N):
            cnt2 = arr[row2][col2]
     
            for i in range(4):
                if i == 0:
                    for j in range(M-1):
                        newR2 = row2 + (dr2[i]-j) # 상하좌우와 다른 점은 방향이 대각선이기 때문에 행과 열을 같이 이동해야된다는 점
                        newC2 = col2 + (dc2[i]-j)
                        if newR2>=0 and newR2<N and newC2>=0 and newC2<N:
                            cnt2 += arr[newR2][newC2]
                if i == 1:
                    for j in range(M - 1):
                        newR2 = row2 + (dr2[i] + j)
                        newC2 = col2 + (dc2[i] - j)
                        if newR2 >= 0 and newR2 < N and newC2 >= 0 and newC2 < N:
                            cnt2 += arr[newR2][newC2]
                if i == 2:
                    for j in range(M - 1):
                        newR2 = row2 + (dr2[i] + j)
                        newC2 = col2 + (dc2[i] + j)
                        if newR2 >= 0 and newR2 < N and newC2 >= 0 and newC2 < N:
                            cnt2 += arr[newR2][newC2]
                if i == 3:
                    for j in range(M - 1):
                        newR2 = row2 + (dr2[i] - j)
                        newC2 = col2 + (dc2[i] + j)
                        if newR2 >= 0 and newR2 < N and newC2 >= 0 and newC2 < N:
                            cnt2 += arr[newR2][newC2]
            lis2.append(cnt2)
     
    #각 파리 개체 수의 합을 상하좌우의 파리 개체수의 합은 lis라는 리스트에 대각선은의 파리 개체수의 합은 lis2라는 리스트에 넣어줌
    #두개의 리스트에서 최댓값을 반환해주어 최대 파리 개체수의 합을 구해줌
    a = max(lis)
    b = max(lis2)
    lis3 = [a, b]
    ans = max(lis3)
    print(f'#{tc} {ans}')