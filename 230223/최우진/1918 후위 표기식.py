exp = input()

esp = {'+':1,'-':1, '*':2, '/':2,'(':0}
isp = {'+':1, '-':1, '*':2, '/':2, '(':4}

ST = []
res = []
for c in exp:
    if c.isupper():
        res.append(c)
    elif c == ')':
        while ST and ST[-1] != '(':  #while ST: -> while len(ST)>0:
            res.append(ST.pop())
        ST.pop()
    else:
        while ST and esp[ST[-1]] >= isp[c]:

            res.append(ST.pop())

        ST.append(c)

while ST:
    res.append(ST.pop())

res = ''.join(map(str, res))
print(res)