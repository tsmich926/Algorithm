def step1(mat):
    ST = []
    result = []
    isp = {'+':1, '-':1, '*':2, '/':2, '(':3}    # 스택 밖에 있을 때
    icp = {'+':1, '-':1, '*':2, '/':2, '(':0}    # 스택 안에 있을 때
 
    for i in mat:
        if i.isalpha():     # 알파벳이면 결과 리스트에 넣어줌
            result.append(i)
        elif i == ')':      # 닫는 괄호일 시
            while ST and ST[-1] != '(':   # 스택에 원소가 있고 마지막 원소가 여는 괄호가 아닐 시
                result.append(ST.pop())   # 여는 괄호가 나올 때까지 스택에서 pop 해서 결과 리스트에 넣어줌
            ST.pop()                      # 여는 괄호까지 pop
        else:
            if ST and icp[ST[-1]] >= isp[i]:     # 스택으로 넣는 값보다 스택 안의 값이 크다면
                while ST and icp[ST[-1]] >= isp[i]:   # 스택 안의 값이 넣는 값보다 작아질때까지 pop
                    result.append(ST.pop())           # 해서 결과 리스트에 넣어줌
                ST.append(i)                     # pop 한 후 push
            else:
                ST.append(i)                     # 스택 안의 값보다 스택으로 넣는 값이 크다면 그냥 넣어줌
    while ST:
        result.append(ST.pop())         # 스택에 남아있는 값이 있다면 결과에 더해줌
    return result


word = input()
print(''.join(step1(word)))      # 하나의 단어로 출력
