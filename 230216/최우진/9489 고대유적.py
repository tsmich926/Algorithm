TC = int(input())
for tc in range(1, TC+1):
    N ,M = list(map(int, input().split()))
 
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    lis1 =[]
    for row in range(N):
        cnt1 = 1
        for col in range(M-1):
                     
                     
            if arr[row][col] == 1 and arr[row][col+1]:
                cnt1 += 1
        lis1.append(cnt1)
     
         
    max_1 = 0
    for i in lis1:
        if i > max_1:
            max_1 = i    
         
                     
                 
             
    lis2 = []
    for row in range(M):
        cnt2 = 1
        for col in range(N-1):
            if arr[col][row] == 1 and arr[col+1][row]:
                cnt2 += 1
        lis2.append(cnt2)
 
         
    max_2 = 0
    for j in lis2:
        if j > max_2:
            max_2 = j 
         
    lis3 = [max_1, max_2]
    max_3 = 0
    for l in lis3:
        if l > max_3:
            max_3 = l
         
    print(f'#{tc} {max_3}')