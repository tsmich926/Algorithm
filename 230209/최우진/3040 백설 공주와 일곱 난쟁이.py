lis = []
for i in range(9):
    num = int(input())
    lis.append(num)


n = len(lis)
lis2 = []
for i in range(1<<n):
    result = []
    for j in range(n):
        if i & (1<<j):
            result.append(lis[j])
        
    if len(result)==7 and sum(result)==100:
        for s in result:
            print(s)