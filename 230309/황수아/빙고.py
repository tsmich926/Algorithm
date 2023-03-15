def checkbing(bing):
    ans = 0
    #가로 검사
    for row in range(5):
        cnt = 0
        for col in range(5):
            if bing[row][col] == 0:
                cnt += 1
        if cnt == 5:
            ans += 1
            if ans >= 3:
                return 1

    #세로검사
    for col in range(5):
        cnt = 0
        for row in range(5):
            if bing[row][col] == 0:
                cnt += 1
        if cnt == 5:
            ans += 1
            if ans >= 3:
                return 1


    #대각선 우 방향
    cnt = 0
    for i in range(5):
        if bing[i][i] == 0:
            cnt += 1
    if cnt == 5:
        ans += 1
        if ans >= 3:
            return 1

    #대각선 좌 방향
    cnt = 0
    for j in range(5):
        if bing[j][4-j] == 0:
            cnt += 1
    if cnt == 5:
        ans += 1
        if ans >= 3:
            return 1


bing = [list(map(int,input().split())) for _ in range(5)]
lst = []
for _ in range(5):
    lst += list(map(int,input().split()))
for i in range(len(lst)):
    for row in range(5):
        for col in range(5):
            if bing[row][col] == lst[i]:
                bing[row][col] = 0
    if i >= 4 and checkbing(bing)==1 : #사회자가 부른 수가 5개 이상이고 3줄이상 빙고가 나왔을때
        print(i+1)
        break