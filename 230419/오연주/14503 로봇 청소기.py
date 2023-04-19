dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

lst[r][c] = -1
count = 1
while lst[r][c] != 1:
    temp = False
    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        newR = r + dr[d]
        newC = c + dc[d]
        if lst[newR][newC] == 0:
            r = newR
            c = newC
            lst[r][c] = -1
            count += 1
            temp = True
            break
    if not temp:
        r += dr[d - 2]
        c += dc[d - 2]

print(count)