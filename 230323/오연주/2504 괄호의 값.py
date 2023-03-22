def check(lst):
    ST = []
    res = 0

    ans = 1
    for i in range(len(lst)):
        if lst[i] == '(':
            ans *= 2
            ST.append(lst[i])
        elif lst[i] == '[':
            ans *= 3
            ST.append(lst[i])

        elif lst[i] == ')':
            if not ST or ST[-1] == '[':
                return 0
            elif lst[i-1] == '(':
                res += ans
            ans = ans // 2
            ST.pop()

        elif lst[i] == ']':
            if not ST or ST[-1] == '(':
                return 0
            elif lst[i-1] == '[':
                res += ans
            ans = ans // 3
            ST.pop()
    if ST:
        return 0
    return res

lst = list(input())
print(check(lst))