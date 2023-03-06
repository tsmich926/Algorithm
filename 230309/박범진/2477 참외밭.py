N = int(input())
ans = []
for _ in range(6):
    R, C = map(int, input().split())
    ans.append((R, C))
# print(ans)


count = [0]*5
for i in ans:
    count[i[0]] += 1
# print(count)


a = 0
b = 0
maxV = 0
for i in ans:
    if count[i[0]] == 1:
        if maxV < i[1]:
            a = i
# print(a)

tmp = ans[::]
for i in tmp:
    if i == a:
        tmp.remove(i)

maxV2 = 0
for i in tmp:
    if count[i[0]] == 1:
        if maxV2 < i[1]:
            b = i
# print(b)

ans.insert(0, ans[5])
ans.insert(7, ans[1])
# print(ans)

c = 0
d = 0
for i in range(1, 7):
    if ans[i] == a and ans[i-1] != b:
        c += ans[i-1][1]
    elif ans[i] == a and ans[i+1] != b:
        c += ans[i+1][1]
    if ans[i] == b and ans[i-1] != a:
        d += ans[i-1][1]
    elif ans[i] == b and ans[i+1] != a:
        d += ans[i+1][1]

# print(c)
# print(d)

res = (a[1]*b[1]) - ((a[1]-d) * (b[1]-c))
print(N*res)