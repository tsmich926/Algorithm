minV = int(input())
maxV = int(input())
lis = []
for i in range(10000):
    lis.append(i**2)
lis2 = []
for j in range(minV, maxV+1):
    if j in lis:
        lis2.append(j)



if len(lis2) == 0:
    print('-1')
    
else:
    print(sum(lis2))
    print(min(lis2))