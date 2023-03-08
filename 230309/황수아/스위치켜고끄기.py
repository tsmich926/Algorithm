def convert(lst,pc):
    if lst[pc] == 0:
        lst[pc] = 1
    else:
        lst[pc] = 0


cnt = int(input()) #스위치 수
Swit = list(map(int,input().split())) #스위치 번호
Swit.insert(0,0)
N= int(input()) #학생수
for i in range(N):
    S, num = map(int,input().split())
    if S == 1:  # 학생이 남자인 경우
        for i in range(num, cnt+1, num):
            if Swit[i] == 1:
                Swit[i] = 0
            else:
                Swit[i] = 1

    else: #학생이 여자인 경우
        convert(Swit, num)
        ran= min(cnt-num,num-1) #범위를 벗어나지 않도록 해줌
        for i in range(1,ran+1): #반복횟수
            if Swit[num-i] == Swit[num+i]:
                if Swit[num-i] ==0:
                    Swit[num-i], Swit[num+i]=1,1
                else:
                    Swit[num-i], Swit[num+i]=0,0
            else:
                break

for i in range(1, cnt, 20):
    print(*Swit[i:i+20])