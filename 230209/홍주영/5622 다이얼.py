import sys
sys.stdin = open('input.txt', 'r')

A = input()
res = {}
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for num in range(3, 11):
    if num == 8 or num == 10:
        res[num] = alp[:4]
        alp = alp[4:]
    else:
        res[num] = alp[:3]
        alp = alp[3:]
cnt = 0
for k, v in res.items():
    for i in A:
        if i in v:
            cnt += k
print(cnt)

