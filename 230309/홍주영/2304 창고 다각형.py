'''
y좌표의 최대값을 구해서
좌, 우 끝부터 진행하면서 기둥 y좌표까지 [x거리 L y좌표 H]
arr 에 덮어줘서 arr 의 합
'''


import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [0 for _ in range(1001)]
L_max = 0
for _ in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    if L > L_max:
        L_max = L
max_L = arr.index(max(arr))

left = 0
for i in range(max_L):
    left = max(left, arr[i])
    arr[i] = left

right = 0
for j in range(L_max, max_L, -1):
    right = max(right, arr[j])
    arr[j] = right

print(sum(arr))