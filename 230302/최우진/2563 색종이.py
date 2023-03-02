N = int(input())

arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    sr, sc = list(map(int, input().split()))
    for row in range(10):
        for col in range(10):
            arr[sr+row][sc+col] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)