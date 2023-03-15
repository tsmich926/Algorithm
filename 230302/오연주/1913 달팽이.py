dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

N = int(input())
se = int(input())
lst = [[0]*N for _ in range(N)]

row = 0
col = 0
d = 0
ai = 0
aj = 0

for i in range(N**2, 0, -1):
    lst[row][col] = i
    if i == se:
        ai = row
        aj = col
    newR = row + dr[d]
    newC = col + dc[d]
    if newR<0 or newR>=N or newC<0 or newC>=N or lst[newR][newC] != 0:
        d = (d+1)%4
    row = row + dr[d]
    col = col + dc[d]

for i in lst:
    print(*i)
print(ai+1, aj+1)