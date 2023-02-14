while True:  # 계속해서 입력됨
    num = str(input()) # 숫자를 str형태로 입력
    if num == '0':  # 0이 나오면 반복문 끝남
        break
    elif num == num[::-1]:
        print('yes')
    elif num != num[::-1]:
        print('no')
