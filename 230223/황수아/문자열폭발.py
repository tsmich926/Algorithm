
#?문자열에서 타겟 문자를 발견하면 계속해서 삭제하고 합침
#?폭발과정이 끝나고 문자열이 남아있으면 남은 문자열 출력, 없으면 FRULA출력


string =input()
target = input()
stack = []

for i in string: #입력받은 문자열에서 하나씩 꺼냄
    stack.append(i)
    if i == target[-1]: #꺼낸 문자열이 타겟 문자열의 마지막 글자와 같을때
        if target == ''.join(stack[-len(target):]): #타겟 문자열과 스택에 들어있는 문자열을 비교.
            #join을 사용해서 붙여서 비교해줄것
            #스택에서 삭제
            del stack[-len(target):]
if stack: #스택이 차있으면 문자열 출력
    print(''.join(stack))
else: #스택이 비어있는 경우
    print('FRULA')