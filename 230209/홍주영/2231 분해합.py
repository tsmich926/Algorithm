# 분해합
'''
주어진 값은 분해합(N)
구해야 하는 값은 가장 작은 생성자(M)


'''

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for i in range(1, N+1):
    sumT = 0
    for j in str(i):
        sumT += int(j)
    if i + sumT == N:
        result = i
        break
    else:
        result = 0
print(result)