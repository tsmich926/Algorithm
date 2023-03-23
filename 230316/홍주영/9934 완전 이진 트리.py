'''
중위순회 문제
k (depth) 별로 순차적으로 줄넘김해주면서 print
'''

import sys
sys.stdin = open('input.txt', 'r')

def inOrder(k):
    global idx
    if k == K:
        return
    inOrder(k+1)
    arr[k].append(nums[idx])
    idx += 1
    inOrder(k+1)

K = int(input())

nums = list(map(int, input().split()))

idx = 0
arr = [[] for _ in range(K)]
inOrder(0)
for i in arr:
    print(*i)
