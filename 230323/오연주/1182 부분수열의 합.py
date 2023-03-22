N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in range(1<<N):
    flst = []
    for j in range(N):
        if i & (1<<j):
            flst.append(lst[j])
    if flst and sum(flst) == S:
        cnt += 1

print(cnt)