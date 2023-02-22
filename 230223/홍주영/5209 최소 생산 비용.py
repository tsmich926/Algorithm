import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def per(k, curS):
    global minS
    if minS < curS:
        return
    if k == N:
        if minS > curS:
            minS = curS
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            per(k+1, curS + arr[i][k])
            visited[i] = False

for tc in range(1, T+1):
    N = int(input())
    visited = [False] * N
    arr = [list(map(int, input().split())) for _ in range(N)]
    minS = 300
    per(0, 0)
    print(f'#{tc}', minS)