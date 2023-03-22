'''
큰 사각형에서 범위 벗어나는 사각형 빼기
'''

import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
width = []
height = []
result = []
for _ in range(6):
    direc, length = map(int, input().split())
    if direc == 1 or direc == 2:
        width.append(length)
        result.append(length)
    else:
        height.append(length)
        result.append(length)

box1 = max(width) * max(height)

max_width = result.index(max(width))
max_height = result.index(max(height))

small_width = abs(result[max_width-1] - result[max_width-5 if max_width == 5 else max_width +1])
small_height = abs(result[max_height-1] - result[max_height-5 if max_height == 5 else max_height +1])

box2 = small_width * small_height
print((box1 - box2)*K)