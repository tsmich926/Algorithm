#자릿수를 반환하는 함수
def jari_sum(n):
    m = str(n)
    sum = 0
    for k in range(len(m)):
        sum += int(m[k])
    return sum

N = int(input())
lst = []
for i in range(N):
    if N == jari_sum(i) + i :
        lst.append(i)
if lst == [] :
    print('0')
else : 
    lst = sorted(lst)
    print(lst[0])