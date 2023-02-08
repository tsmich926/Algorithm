N = int(input())
i = 1
while i < 1000001:
    sumV = 0
    sumN = 0
    min_num = 0
    # 각자리의 숫자 더하기
    for v in range(len(str(i))):
        sumV += int(str(i)[v])
   
    sumN += i + sumV  # 원래 숫자 + 각자리의 숫자를 다 더한값 = 분해합
    
    #입력한 숫자가 분해합이면 min_num에 저장후 종료(최소임), 아니면 1씩더해서 반복
    if N == sumN:
        min_num = i
        break
    else:
        i += 1
print(min_num)