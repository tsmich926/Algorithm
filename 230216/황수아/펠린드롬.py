while True:
    n = input()
    stack = []
    compare = ''
    if n == '0':
        break
    else:
        for i in n:
            stack.append(i)
        for i in range(len(stack)):
            compare += stack.pop()
        if compare == n:
            print('yes')
        else:
            print('no')