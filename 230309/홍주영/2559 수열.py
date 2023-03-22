'''
더해가면서
앞의 리스트부분 제거
브루트포스
'''

import sys
sys.stdin = open('input.txt', 'r')
ans = []
N, K = map(int, input().split())
lis = list(map(int, input().split()))

ans.append(sum(lis[:K]))
for i in range(N-K):
    ans.append(ans[i] - lis[i] + lis[i+K])
print(max(ans))
