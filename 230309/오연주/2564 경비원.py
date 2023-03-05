c, r = map(int, input().split())
N = int(input())
lst = []

for _ in range(N+1):
    n1, n2 = map(int, input().split())
    if n1 == 1:
        lst.append(n2)
    if n1 == 2:
        lst.append(c+r+c-n2)
    if n1 == 3:
        lst.append(c+r+c+r-n2)
    if n1 == 4:
        lst.append(c+n2)

sumV = 0
for i in lst[:N]:
    dist = abs(i-lst[-1])
    rest = 2*(c+r)-dist

    sumV+=min(dist, rest)

print(sumV)