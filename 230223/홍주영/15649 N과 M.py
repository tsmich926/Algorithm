'''
수업시간에 배운 순열
'''

import sys
sys.stdin = open('input.txt', 'r')

def per(k):
    if k == M:
        for i in range(M):
            idx = a[i]
            print(arr[idx], end=' ')
        print()
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            a[k] = i
            per(k+1)
            visited[i] = False

N, M = map(int, input().split())
arr = []
for num in range(1, N+1):
    arr.append(num)

a = [-1]*N
visited = [False]*N
per(0)