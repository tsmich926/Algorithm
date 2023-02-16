import sys
sys.stdin = open('input.txt', 'r')

# Pelindrome 수 배운거
while True:
    tc = input()
    if tc == '0':  # 길이가 0이면 X
        break
    for i in range(len(tc)//2):
        if tc[i] != tc[-(i+1)]:   # 첫 값과 끝 값이 다르면 no
            print('no')
            break
    else:
        print('yes')            # 아니면 yes


# 범위를 2로나눈 몫으로 해주는 이유

# tc의 길이가 홀수면 중앙값을 기준으로 대칭되는데, 중앙값은 굳이 조건문을 안 돌아도 되기 때문에
