N = input()
M = input()
N = int(N)
M = int(M)
lst = []
sum = 0
for i in range(1,100+1):
    if N <= i*i <= M :
        lst.append(i*i)
        sum += i*i
if sum == 0 and lst == []:
    print('-1')
else:
    print(sum)
    print(lst[0])