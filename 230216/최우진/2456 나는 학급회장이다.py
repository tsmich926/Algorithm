N = int(input())
lis2 = []
for i in range(N):
    lis = list(map(int, input().split()))
    lis2.append(lis)   #제곱해주기 전 리스트

lis3 = []
for k in range(len(lis2)):
    for o in range(3):
        lis3.append((lis2[k][o])**2)  #제곱실행

def list_chunk(lst,n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
lis3 = list_chunk(lis3, 3) # 다시 3개씩 묶어줌

#제곱해주기 전 후보들의 총 투표수 합
a_1 = 0
for j in lis2:
    a_1 += j[0]

b_1 = 0
for j in lis2:
    b_1 += j[1]

c_1 = 0
for j in lis2:
    c_1 += j[2]

lis4 = [a_1 ,b_1, c_1]
lis4_max = max(lis4)  #최댓값

#제곱해준 후 후보들의 총 투표수 합
a = 0
for j in lis3:
    a += j[0]

b = 0
for j in lis3:
    b += j[1]

c = 0
for j in lis3:
    c += j[2]



if lis4.count(lis4_max) == 1:
    print(lis4.index(lis4_max)+1, lis4_max)
    

else:
    if a==b and b==c and a==c:
        print('0', a_1)
    else:
        lis5 = [a,b,c]
        maxV = 0
        for l in lis5:
            if l > maxV:
                maxV = l  #제곱한 것의 합의 최댓값

    # d =0
    # for j in lis2:
    #     d += j[lis4.index(maxV)]
    d = lis5.index(maxV)+1

    print(d, lis4[lis5.index(maxV)])