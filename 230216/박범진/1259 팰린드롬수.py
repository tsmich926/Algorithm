while True:    # 참일시 계속 실행
    N = input()    # 0을 입력하면 종료
    if N == '0':
        break
    elif N == N[::-1]:
        print('yes')
    else:
        print('no')