'''
겹치는 부분만 찾아서
N *100 에서 겹치는 부분 빼주고 출력
'''


import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = list(map(int, input().split()))
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] += 1                 # 색종이의 범위에 1씩올려줌
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] > 1:           # 겹치는 부분에 대해 값-1 만큼 모두 더해줌
            cnt += arr[i][j] -1
ans = N*100 - cnt  # 전체에서 겹친 부분 cnt 한 만큼 빼줌
print(ans)




