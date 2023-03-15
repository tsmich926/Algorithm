N, K = map(int, input().split())

lst = list(range(1, N+1))
rear = -1
result = []


for i in range(N):
    rear += K
    while rear >= len(lst):
        rear = rear - len(lst)
    v = lst.pop(rear)
    rear -= 1
    result.append(v)


print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='')
print('>', end='')