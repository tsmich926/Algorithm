arr = [list(map(int, input().split())) for _ in range(5)]

# print(arr)

lis = []
for i in range(5):
    lis.append(list(map(int, input().split())))

ans_lis = []
for i in lis:
    for j in range(5):
        ans_lis.append(i[j])
# print(ans_lis)



visited = [[1]*5 for _ in range(5)]



for i in ans_lis:   # 사회자가 수를 하나씩 부르는데
    # sumV = 0
    for row in range(5):
        for col in range(5):  #arr의 각지점에서
            if arr[row][col] == i: #사회자가 부른 수랑 일치하면
                # sumV = 0
                visited[row][col] -= 1 #visited에서 1씩 빼줄 것임
    sumV = 0
    
                
    for r in range(5):   # 행별로 visited 탐색할 때
        cnt1 = 0
        for c in range(5):
            if visited[r][c] == 0:  #0이면 cnt에 +1
                cnt1 += 1
                if cnt1 == 5: 
                    sumV += 1
                    
                    
    
    for r in range(5):   # 열별
        cnt2 = 0
        for c in range(5):
            if visited[c][r] == 0:
                cnt2 += 1
                if cnt2 == 5:
                    sumV += 1
                    
                    
    
    cnt3 = 0      # 대각선 1
    for r in range(5):
        for c in range(5):
            if r == c:
                if visited[r][c] == 0:
                    cnt3 += 1
                    if cnt3 == 5:
                        sumV += 1
                        
                        
    
    cnt4 = 0      # 대각선 2
    for r in range(5):
        for c in range(5):
            if c == 4-r:
                if visited[r][c] == 0:
                    cnt4 += 1
                    if cnt4 == 5:
                        sumV += 1
                                

    if sumV >= 3:
        print(ans_lis.index(i)+1)
        break