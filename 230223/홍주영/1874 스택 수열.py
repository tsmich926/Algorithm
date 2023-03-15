'''
push : +
pop : -
12345678
8
ST = [1257
list = 43687521
++++--++-++-----
'''

import sys
sys.stdin = open('input.txt', 'r')


lis = []
ST = []
n = int(input())

res = []
ans = []
for i in range(n):
    num = int(input())
    lis.append(num)

i = 1
k = 0
while i < n+1:
    if ST and  ST[-1] == lis[k]:
        k += 1
        res.append(ST.pop())
        ans.append('-')
    else:
        ST.append(i)
        ans.append('+')
        i+= 1

while ST:
    res.append(ST.pop())
    ans.append('-')

if res == lis:
    for j in ans:
        print(j)
else:
    print('NO')

