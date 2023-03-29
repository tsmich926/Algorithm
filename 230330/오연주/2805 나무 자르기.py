import sys
imput = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()

l = 1
r = lst[-1]

while l<=r:
    m = (l+r)//2

    sumV = 0
    for i in lst:
        if i >= m:
            sumV += i-m

    if sumV >= M:
        l = m + 1
    else:
        r = m-1
print(r)
