#3번의 방향전환후 시작점으로 다시 되돌아와야한다. + 되도록 많이 여러개의 디저트를 먹고 와야함
# 디저트가 겹치면(같은 숫자의 디저트) 안된다.
#한 개의 카페에서 디저트를 먹으면 안된다.
#다시 되돌아가기 안됨.

#돌 수 있는 대각선 방향 표시
di=[1,1,-1,-1,1]
dj=[-1,1,1,-1,1]

#(꺾이는 방향 전환횟수,row,col,값)
# V 배열에 이제까지 먹은 디저트의 숫자를 저장해서 중복된 디저트를 먹지 않도록 한다.
def dfs(n, ci, cj, v):
    global ans, si, sj
    if n>3:
        return
    if n==3 and (ci,cj)==(si,sj) and ans<len(v): #도착지점과 시작지점이 같아지면+전보다 여러개의 디저트를 먹게되면
        ans = len(v) #ans의 값 갱신

    for dr in range(n, n+2): # 계속 원래 방향으로 이동을 하거나 방향전환을 해서 꺾거나
        ni,nj = ci+di[dr], cj+dj[dr]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v: #좌표가 범위안이고 새로운 디저트이면
            dfs(dr, ni, nj, v + [arr[ni][nj]])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] #디저트의 번호가 적힌 배열 입력받기
    ans = -1  #디저트를 먹을 수 없는 경우 -1이 출력되도록..
    # (0,0)부터 (N-1,N-1)까지 돈다
    for si in range(N):
        for sj in range(N):
            dfs(0, si, sj, [])

    print(f'#{test_case} {ans}')
