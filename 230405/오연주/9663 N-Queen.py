def promising(q):
    for i in range(q):
        if ST[i] == ST[q]:
            return False
        if abs(q - i) == abs(ST[q] - ST[i]):
            return False
    return True


def check(k):
    global cnt
    if k == N:
        cnt += 1
        return

    for i in range(N):
        ST[k] = i
        if promising(k):
            check(k+1)

N = int(input())
cnt = 0
ST = [0] * N
check(0)
print(cnt)