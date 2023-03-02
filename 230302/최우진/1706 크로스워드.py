R, C = list(map(int, input().split()))

arr = [input() for _ in range(R)]

res = []
for row in range(R):
    lis = []
    for col in range(C):
        if arr[row][col].isalpha():
            lis.append(arr[row][col])
        if arr[row][col] == '#':
            if len(lis) >= 2:
                res.append(lis)
            lis = []


    if len(lis) >= 2:
        res.append(lis)

# print(res)

res2 = []
for row in range(C):
    lis2 = []
    for col in range(R):
        if arr[col][row].isalpha():
            lis2.append(arr[col][row])
        if arr[col][row] == '#':
            if len(lis2) >= 2:
                res2.append(lis2)
            lis2 = []


    if len(lis2) >= 2:
        res2.append(lis2)
# print(res2)

ans_lis = []
for i in res:
    ans_lis.append(i)
for i in res2:
    ans_lis.append(i)

a = sorted(ans_lis)
a = ''.join(map(str, a[0]))
print(a)