def check(lst):
    fcnt = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if lst[i][j] == 0:
                cnt += 1
        if cnt == 5:
            fcnt += 1

    for j in range(5):
        cnt = 0
        for i in range(5):
            if lst[i][j] == 0:
                cnt += 1
        if cnt == 5:
            fcnt += 1
    cnt1 = 0
    for i in range(5):
        if lst[i][i] == 0:
            cnt1 += 1
    if cnt1 == 5:
        fcnt += 1
    cnt2 = 0
    for i in range(5):
        if lst[i][4-i] == 0:
            cnt2 += 1
    if cnt2 == 5:
        fcnt += 1
    return fcnt





mine = [list(map(int, input().split())) for _ in range(5)]
new = []
nums = []
ans = 0

for _ in range(5):
    lst = list(map(int, input().split()))
    for i in lst:
        nums.append(i)

for num in nums:
    ans += 1
    for i in range(5):
        for j in range(5):
            if mine[i][j] == num:
                mine[i][j] = 0
                if check(mine) >= 3:
                    new.append(ans)

print(new[0])