def ispair(sen):
    stack = []
    for s in sen:
        if s == '(':
            stack.append(s)

        elif s == ')':
            if len(stack) == 0:
                return 'no'
            t = stack.pop(-1)
            if t != '(':
                return 'no'

        if s == '[':
            stack.append(s)
        elif s == ']':
            if len(stack) == 0:
                return 'no'
            t = stack.pop(-1)
            if t != '[':
                return'no'
    if len(stack) > 0:
        return 'no'
    return 'yes'

while True:
    sen = input()
    if sen == '.':
        break
    print(ispair(sen))