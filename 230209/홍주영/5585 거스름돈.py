import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
money = [500, 100, 50, 10, 5, 1]
res = 1000 - N
cnt = 0
for i in range(len(money)):
    if res // money[i] != 0:
        cnt += res // money[i]
        res -= money[i]*(res//money[i])
print(cnt)
