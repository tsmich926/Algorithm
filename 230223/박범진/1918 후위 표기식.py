def postfix(sen):
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    ST = []
    result = ''

    def postfix(sen):
        isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
        icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
        ST = []
        result = ''

        for i in sen:
            if i.isalpha():
                result += i

            else:
                if i == ')':
                    while ST and ST[-1] != '(':
                        result += ST.pop()
                    ST.pop()

                elif ST and isp[ST[-1]] > icp[i]:
                    while ST and isp[ST[-1]] >= icp[i]:
                        result += ST.pop()
                    ST.append(i)

                else:
                    ST.append(i)

        while ST:
            result += ST.pop()

        return result

    sen = list(input())
    print(postfix(sen))