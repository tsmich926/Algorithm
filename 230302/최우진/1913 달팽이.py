N = int(input())
F = int(input())

arr = [[0]*N for _ in range(N)]


dr = [1,0,-1,0]
dc = [0,1,0,-1]

sr = 0
sc = 0
dist = 0

for i in range(N*N, 0, -1):
    arr[sr][sc] = i
    sr += dr[dist]
    sc += dc[dist]

    if sr < 0 or sr >=N or sc < 0 or sc >= N or arr[sr][sc] != 0:
        sr -= dr[dist]
        sc -= dc[dist]
        dist = (dist+1) % 4
        sr += dr[dist]
        sc += dc[dist]

for row in arr:
    print(*row)

for i in range(N):
    for j in range(N):
        if arr[i][j] == F:
            print(i+1, j+1)