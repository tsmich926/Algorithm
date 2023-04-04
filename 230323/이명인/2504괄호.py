def calculate_value(s):
    stack = []
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                return 0
            stack.pop()
            stack.append(2)
        elif c == ']':
            if not stack or stack[-1] != '[':
                return 0
            stack.pop()
            stack.append(3)
        else:
            return 0

        while len(stack) >= 2 and isinstance(stack[-1], int) and isinstance(stack[-2], int):
            b, a = stack.pop(), stack.pop()
            stack.append(a + b * (3 if a == '[' else 2))

    if len(stack) != 1 or not isinstance(stack[0], int):
        return 0

    return stack[0]


s = input()
print(calculate_value(s))