'''
남학생 -> 스위치 번호가 자기가 받은 수의 배수이면 상태를 바꿈
여학생 -> 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를
포함하는 구간을 찾아서 상태를 바꿈 이 때, 스위치 개수는 항상 홀수'''

import sys
sys.stdin = open('input.txt', 'r')

def pelindrome(num):
    k = 1
    if status[num-1] == 1:
        status[num-1] = 0
    else:
        status[num-1] = 1
    while 0<= num-1-k and num-1+k < len(status):
        if status[num-1-k] == status[num-1+k]:
            if status[num-1-k] == 1:
                status[num-1-k] = status[num-1+k] = 0
            else:
                status[num-1-k] = status[num-1+k] = 1
            k += 1

        else:
            return status

def func(s):
    if s == 1:
        for i in range(num-1, len(status), num):
            if status[i] == 1:
                status[i] = 0
            else:
                status[i] = 1
        return status
    if s == 2:
        return pelindrome(num)



switch = int(input())
status = list(map(int, input().split()))
N = int(input())
for _ in range(N):
    s, num = map(int, input().split())
    func(s)
d = 0
while True:
    if len(status) - d >= 20:
        print(*status[d:20+d])
    else:
        print(*status[d:])
        break

    d+= 20
