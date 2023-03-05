K = int(input())
lst1 = []
lst2 = []
lst3 = []

for _ in range(6):
    n1, n2 = map(int, input().split())
    if n1 == 1 or n1 == 2:
        lst1.append(n2)
    else:
        lst2.append(n2)
    lst3.append(n2)
lst3 = lst3*2
m1 = 0
m2 = 0
for i in range(len(lst3)):
    if lst3[i] == max(lst1):
        m1 = abs(lst3[i-1]-lst3[i+1])
        break
for i in range(len(lst3)):
    if lst3[i] == max(lst2):
        m2 = abs(lst3[i-1]-lst3[i+1])
        break


area = max(lst1)*max(lst2)-(m1*m2)
print(area*K)