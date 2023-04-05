import sys
sys.stdin = open('input.txt', 'r')

def check(k):
    for i in range(k):
        if row[k] == row[i] or abs(row[k] - row[i]) == abs(k-i):
            return False
    return True

def dfs(k):
    global ans

    if k == N:
        ans += 1
        return
    else:
        for i in range(N):
            row[k] = i
            if check(k):
                dfs(k+1)

N = int(input())
ans = 0
row = [0]*N
dfs(0)
print(ans)