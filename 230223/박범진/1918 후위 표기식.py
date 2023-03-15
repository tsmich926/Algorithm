def postfix(sen):
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}    # 새로 문자가 들어왔을 때 내부에서 비교하기 위한 것
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}    # 새로 문자를 집어 넣을 때 밖에서 비교하기 위한 것
    ST = []
    result = ''

    for i in sen:
        if i.isalpha():    # 알파벳이면 result에 더하기
            result += i

        elif i == ')':    # )이 나오면 (가 나올때 까지 ST를 pop해서 result에 더하기
            while ST and ST[-1] != '(':
                result += ST.pop()
            ST.pop()    # 마지막에 (를 pop

        elif ST and isp[ST[-1]] >= icp[i]:    # ST안에 들어있는 연산자보다 우선순위가 밀리거나 같을 때
            while ST and isp[ST[-1]] >= icp[i]:
                result += ST.pop()    # 안밀릴 때 까지 ST를 pop해서 result에 더하기
            ST.append(i)    # 그리고 우선순위가 밀리는 연산자 ST에 추가하기

        else:
            ST.append(i)    # 우선순위가 밀리지 않는 연산자일 경우 ST에 추가

    while ST:
        result += ST.pop()    # 마지막에 ST에 남아있는 연산자들 다 result에 더하기

    return result

sen = input()
print(postfix(sen))