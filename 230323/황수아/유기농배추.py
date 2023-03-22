import sys
sys.setrecursionlimit(10000)


def bugfinder(x,y):
    #상하좌우
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    for i in range(4):
        newr = x+dr[i]
        newc = y+dc[i]
        if (0<=newr<N) and (0<=newc<M): #범위체크 유효범위인지
            if arr[newr][newc] == 1: #상하좌우에 배추가 심어져 있는가?를 검사
                arr[newr][newc] = -1 #인접배열은 처음에 벌레를 한마리 더해주고 그뒤에는 안더해줘도 된다
                bugfinder(newr, newc) #본 배열위치의 상하좌우를 검사하다 배추를 발견하면 그곳의 상하좌우도 검사해야한다

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr= [[0]*M for _ in range(N)]
    bug = 0
    for i in range(K): #배추가 심어진 갯수만큼 위치를 입력받음
        x,y = map(int,input().split())
        arr[x][y] = 1 #배추 심었다는 것을 표시해 준다

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: # 배추가 심어져있으면 함수실행
                arr[i][j] = -1  #visit배열을 만들어 방문표시하는대신 -1을 넣어 방문표시한다. 1이면 배추가 있고 0이면 배추가 없고 -1이면 방문
                bug += 1  # 함수를 실행할때마다 벌레를 한마리씩 더해준다
                bugfinder(i,j)

    print(bug)
