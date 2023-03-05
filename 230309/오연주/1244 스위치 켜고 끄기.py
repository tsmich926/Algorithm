sw = int(input())
swof = list(map(int, input().split()))
N = int(input())

for _ in range(N):
    p, num = map(int, input().split())
    if p == 1:
        for i in range(1, sw//num+1):
            if swof[num*i-1] == 0:
                swof[num*i-1] = 1
            else:
                swof[num*i-1] = 0
    if p == 2:
        for i in range(sw):
            if 0<=num-1-i<sw and 0<=num-1+i<sw:
                if swof[num-1-i] == swof[num-1+i]:
                    if swof[num-1-i] == 0:
                        swof[num-1-i], swof[num-1+i] = 1, 1
                    else:
                        swof[num-1-i], swof[num-1+i] = 0, 0
                if swof[num-1-i] != swof[num-1+i]:
                    break

for i in range(sw):
    print(swof[i], end=' ')
    if i == 19 or i == 39 or i == 59 or i == 79:
        print()