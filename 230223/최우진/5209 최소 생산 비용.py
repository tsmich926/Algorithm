def perm(k, curS):
    global minV

    if minV < curS:
        return

    if k == N:
        if minV > curS:
            minV = curS

    for j in range(N):  # 사용하지 않은 숫자를
        if used[j] == 0:  # used에서 순서대로 검색

            used[j] = 1  # j번째 자리 숫자 사용으로 표시
            perm(k + 1, curS + arr[j][k])
            used[j] = 0  # j번 자리 숫자를 다른 자리에서 쓸 수 있게


#
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minV = 1000000
    used = [0] * N
    perm(0, 0)

    print(f'#{tc} {minV}')