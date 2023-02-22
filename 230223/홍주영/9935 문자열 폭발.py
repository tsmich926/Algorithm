'''
주어진 문자열에서 특정 문자열을 빼주는 문제
비밀번호 문제와 비슷함

'''
import sys
sys.stdin = open('input.txt', 'r')

s = list(input())           # 주어진 문자열
bomb = list(input())        # 두번째 줄에 주어진 문자열(제거할 대상 문자)
ST = []
for i in range(len(s)):
    ST.append(s[i])          # 스택에 모두 집어 넣다가
    if ST and ST[-len(bomb):] == bomb:  # 스택 끝중에 bomb 만큼의 길이와 bomb 가 같으면
        for _ in range(len(bomb)):      # 그만큼의 길이를 스택에서 pop ( 스택에 들어있는 bomb 를 제거 )
            ST.pop()

if ST:                      # 스택에 값이 남아있으면 출력
    print(''.join(ST))
else:                       # 아니면 FRULA 를 출력
    print('FRULA')