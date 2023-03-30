# 1. 팀이 몇 명인지에 따라서 그 사람들의 조합이 필요함
# 2. 그 조합을 가지고 하나하나 순열을 만들어줌
# 3. 순열의 값을 다 더하고 정답리스트에 넣은 후 앞뒤를 차례차례비교하면 끝


def per(node, ARR):
    global tmp
    if node == L:
        tmp += arr[res[0]][res[1]]
        return tmp
    else:
        for j in range(M):
            if V[j] == False:
                res[node] = ARR[j]
                V[j] = True
                per(node+1, ARR)
                V[j] = False



# s = 이전 단계에서 결정한 값
def comb(n, s):
    if n == K:
        global tmp
        global ans
        # print(result)
        tmp = 0
        per(0, result)
        ans.append(tmp)
        return

    else:
        for i in range(s+1, N+1):
            result[n] = i
            comb(n+1, i)



T = int(input())
for test_case in range(1, T+1):

    # comb용
    N = int(input())               # 원소의 개수
    K = N//2                       # 조합의 크기
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    result = [-1] * K              # 결과들이 저장될 리스트
    visited = [False] * (N+1)      # 방문 리스트


    # per용
    M = len(result)                # 원소의 개수
    L = 2                          # 조합의 크기
    res = [-1] * L                 # 결과들이 저장될 리스트
    V = [False] * M                # 방문 리스트


    ans = []
    tmp = 0
    comb(0, 0)

    middle = len(ans)//2
    i = 0
    minV = 20000
    while i < middle:
        if minV > abs(ans[0+i] - ans[len(ans)-i-1]):
            minV = abs(ans[0+i] - ans[len(ans)-i-1])
        i += 1

    print(f'#{test_case} {minV}')