'''
가장 큰 증가하는 부분수열
DP 문제

'''

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lis = list(map(int, input().split()))

dp = [0]*N

dp[0] = lis[0]

for i in range(N):
    for j in range(i):
        if lis[i] > lis[j]:
            dp[i] = max(dp[i], dp[j]+lis[i])
print(max(dp))