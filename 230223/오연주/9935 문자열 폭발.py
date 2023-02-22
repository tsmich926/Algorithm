word = list(input())
bomb = input()
ST = []    # 스택 생성

for c in word:
    ST.append(c)    # 단어 하나씩 스택에 넣으면서
    if ''.join(ST[-len(bomb):]) == bomb:    # 스택의 뒤부터 폭발 문자열의 길이만큼 세서 단어가 같다면
        for i in range(len(bomb)):      # 폭발 문자열 단어 길이만큼 삭제
            ST.pop()

if len(ST) == 0:     # 스택에 남은 문자열이 없으면 FRULA 출력
    print('FRULA')
else:
    print(''.join(ST))
