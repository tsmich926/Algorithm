'''
#으로 패딩 해주고 길이가 1인 경우는 낱말이 아니기 때문에
길이 2이상인 값들을 res 에 추가시키고 사전순 정렬
정렬 후 0번째 인덱스 출력
'''

import sys
sys.stdin = open('input.txt', 'r')

R, C = map(int, input().split())

arr = [list(map(str, input() + '#')) for _ in range(R)] + [list(map(str, '#'*(C+1)))]
res = []
for i in range(R+1):           # 가로
    word = ''
    for j in range(C+1):
        if arr[i][j].isalpha():
            word += arr[i][j]
        else:
            if word and len(word) >= 2:
                res.append(word)
            word = ''

for j in range(C+1):            # 세로
    word = ''
    for i in range(R+1):
        if arr[i][j].isalpha():
            word += arr[i][j]
        else:
            if word and len(word) >= 2:
                res.append(word)
            word = ''

res.sort()
print(res[0])