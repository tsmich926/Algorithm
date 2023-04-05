def cal(num1, ope, num2):
    if ope == '+':
        return num1+num2
    elif ope == '-':
        return num1-num2
    elif ope == '*':
        return num1*num2
    elif ope == '//':
        if num1<0 and num2>0:
            return -(-num1//num2)
        return num1//num2


def check(k, curV):
    global minV
    global maxV

    if k == N-1:
        if curV <= minV:
            minV = curV
        if curV >= maxV:
            maxV = curV
        return


    for i in range(4):
        if opelst[i]:
            opelst[i] -= 1
            check(k+1, cal(curV, op[i], numlst[k+1]))
            opelst[i] += 1



N = int(input())
op = ['+', '-', '*', '//']
numlst = list(map(int, input().split()))
opelst = list(map(int, input().split()))
maxV = -10000000000
minV = 10000000000

check(0, numlst[0])
print(maxV)
print(minV)