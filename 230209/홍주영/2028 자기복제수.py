# 자기복제수

'''
어떤 자연수 N을 제곱햇을때, 맨 뒷자리에 원래의 수 N이 다시나타나면 자기복제수
ex) 5 ** 2 = 25 이고, 끝자리가 5이므로 자기 복제수
    76 ** 2  = 5776 이므로 자기 복제수
    자연수 N이 주어졌을 때, 그 수가 자기복제수인지 아닌지 출력
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ANS = N**2
    if str(N) == str(ANS)[len(str(ANS))-len(str(N)):]:
        print('YES')
    else:
        print('NO')