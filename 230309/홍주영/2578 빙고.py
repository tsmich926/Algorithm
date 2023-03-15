import sys
sys.stdin = open('input.txt', 'r')

def bingo():
    a = 0
    result = 0
    cnt = 1
    while a < 25:
        for i in range(5):
            for j in range(5):
                if arr[i][j] == res[a]:
                    arr[i][j] = 0
                    cnts[i] += 1
                    cnts[j + 5] += 1
                    if i == j:
                        cnts[10] += 1
                    if i + j == 4:
                        cnts[11] += 1
                    break

        while max(cnts) == 5:
            t = cnts.index(max(cnts))
            cnts[t] = 0
            result += 1
            if result >= 3:
                return cnt
        a += 1
        cnt += 1


arr = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]
res = sum(ans, [])

cnts = [0]*12
print(bingo())