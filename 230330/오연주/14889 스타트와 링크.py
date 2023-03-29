def par(k):
    global minV
    if k == N:
        if result.count(1) == N//2:
            tlst = []
            nlst = []
            for i in range(N):
                if result[i] == 1:
                    tlst.append(i)
                else:
                    nlst.append(i)
            sumV = 0
            sumV2 = 0
            for i in tlst:
                for j in tlst:
                    if i != j:
                        sumV += lst[i][j]
            for i in nlst:
                for j in nlst:
                    if i != j:
                        sumV2 += lst[i][j]
            if minV > abs(sumV-sumV2):
                minV = abs(sumV-sumV2)

        return
    result[k] = 1
    par(k+1)
    result[k] = 0
    par(k+1)



N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
result = [-1]*N
minV = 100*20*20
par(0)

print(minV)

