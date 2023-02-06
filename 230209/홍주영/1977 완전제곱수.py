# 완전 제곱수
'''
M이상 N 이하의 자연수중 완전 제곱수찾기
합, 최솟값 출력

'''

import sys
sys.stdin = open('input.txt', 'r')

M = int(input())
N = int(input())
sumI = 0
minI = N
for i in range(M, N+1):
    if int(i**(0.5))**2 == i:
        sumI += i
        if i < minI:
            minI = i

if sumI != 0:
    print(sumI)
    print(minI)
else:
    print(-1)