#괄호입력
str = input()
l = []
result = 0
n = 1

#입력받은 괄호꺼내기
# 닫힌 괄호가 맞는지 확인
# 열린 다음 닫힌 경우에만 값 더하기
# 괄호를 닫은후에는 그 괄호가 가지는 수만큼 나누어주고 l에서 괄호빼기
for i in range(len(str)):
    if str[i] == '(':
        l.append('(')
        n *= 2
    elif str[i] == '[':
        l.append('[')
        n *= 3
    elif str[i] == ')':
        if not l or l[-1] != '(':
            result = 0
            break
        if str[i-1] == '(':
            result += n
        l.pop()
        n //= 2
    elif str[i] == ']':
        if not l or l[-1] != '[':
            result = 0
            break
        if str[i-1] == '[':
            result += n
        l.pop()
        n //= 3
if l:
    result = 0
# 괄호가 남아있다면 결과를 0으로

print(result)