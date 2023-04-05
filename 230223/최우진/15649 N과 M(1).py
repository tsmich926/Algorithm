N, M = list(map(int, input().split()))


def comb(k):
    if k >= M:
        print(*candidate)
        return

    for i in range(1, N+1):
        if i not in candidate:
            candidate.append(i)
            comb(k + 1)
            candidate.pop()


candidate = []
comb(0)