x, y = list(map(int, input().split()))
N = int(input())

arr = []
for _ in range(N+1):
    d, l = list(map(int, input().split()))

    if d == 1:
        arr.append(y+l)
    if d == 2:
        arr.append(-l)
    if d == 3:
        arr.append(y-l)
    if d == 4:
        arr.append(-x-(y-l))

ans_lis = []
sum_l = 2*x+2*y
for i in range(N):
    value1 = abs(arr[N] - arr[i])
    value2 = sum_l - value1
    if value1 < value2:
        ans_lis.append(value1)
    elif value1 > value2:
        ans_lis.append(value2)
    else:
        ans_lis.append(value1)
# print(ans_lis)

print(sum(ans_lis))