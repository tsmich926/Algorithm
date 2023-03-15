# 문제 이해못함
N = int(input())
lst = list(range(8, 0, -1))  # 1에서 8까지의 리스트 생성
ST = []


for i in range(N):
    num = int(input())
    if not ST:                 # 스택에 아무것도 없을 땐
        for _ in range(num):   # 입력된 숫자만큼 push
            ST.append(lst.pop())
            print('+')

    elif ST[-1] < num:          # 스택 안의 값이 입력값보다 작으면
        while ST[-1] != num:
            ST.append(lst.pop())  # 본 리스트에서 스택으로 그 숫자까지 push
            print('+')


    elif ST[-1] > num:          # 스택 안의 값이 입력값보다 크면
        while ST[-1] != num:    # 입력값 전까지 스택에서 빼서 리스트에 넣어줌
            v = ST.pop()
            print('-')
            lst.append(v)

    if ST[-1] == num:   # 스택의 마지막 값이 입력값과 같다면
        ST.pop()
        print('-')
