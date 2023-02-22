# 분해합
'''
주어진 값은 분해합(N)
구해야 하는 값은 가장 작은 생성자(M)
주의할 점 : print(result) 를 맨 마지막에 출력했었는데 사실 if문 안에서 출력하면
           result 값이 최소를 요구하기 때문에 굳이 더 반복문을 돌 필요가 없음
'''

N = int(input())


for i in range(1, N+1):
    sumT = 0
    for j in str(i):           # 입력값이 216 일때, 임의의 i를 str 으로 만들어서 for 문 반복(반복문은 1부터 입력값까지)
        sumT += int(j)         # 각자리의 str 을 sumT에 더해주고
    if i + sumT == N:          # 만약 각자리의 합(sumT)과 현재의 본인(i)를 더한 값이 입력값(N)이면
        result = i             # i를 result 에 저장하고 반복문 탈출
        print(result)
        break                  # 아니면 result = 0 으로 초기화
    else:
        result = 0
