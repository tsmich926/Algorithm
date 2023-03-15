'''
일자로 펼쳐서 각 방향의 case를 고려해줘 더해줌
'''

import sys
sys.stdin = open('input.txt', 'r')

L, H = map(int, input().split())
lis = []
N = int(input())
for _ in range(N+1):
    direction, length = map(int,  input().split())
    if direction == 1:
        lis.append(H + length)
    elif direction == 2:
        lis.append(-length)
    elif direction == 3:
        lis.append(H - length)
    else:
        lis.append(length - L - H)

total  = 2*(L+H)
ans = 0
for i in range(N):
    value = lis[N] - lis[i]
    if value < 0:
        value = abs(value)
    if total - value > value:
        ans += value
    else:
        ans += total - value

print(ans)
