'''
계산기 문제
직접 스택과 결과에 이동을 시켜보며 출력 값처럼 만들어 주겠다는 생각으로 접근

'''

import sys
sys.stdin = open('input.txt', 'r')
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}


def step1(s):
    ST = []
    result = []
    for i in s:
        if i.isupper():                          # 문제에서 알파벳은 대문자라고 주어짐
            result.append(i)
        elif i == ')':
            while ST and ST[-1] != '(':           # 이 부분 코드가 잘못되었는데 test case 통과 반례 : ***)
                result.append(ST.pop())           # 이 1918번 문제는 옳은 괄호만 표시되기 때문
           ST.pop()
        else:
            while ST and isp[ST[-1]] >= icp[i]:    # else 문에는 스택의 끝값이 밖의 값보다 같거나 클때동안 append 하고
                result.append(ST.pop())
            ST.append(i)                           # 밖의 i값을 ST에 append
    while ST:
        result.append(ST.pop())                    # 스택에 값이 남아있으면 전부 result 에 pop

    return result
s = input()
res = step1(s)
print(''.join(res))
