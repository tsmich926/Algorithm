M = int(input())
N = int(input())
sumV = 0
min_lst = []

# 최대 제곱수가 10000이기 때문에 i의 최댓값은 100
for i in range(1, 101):
    if M <= i**2 <= N:
        sumV += i**2
        min_lst.append(i**2) # 최솟값을 구하기 위해 리스트에 추가해서 마지막에 구하기
# 제곱수가 하나라도 있으면 sumV가 0보다 클 것이고, 0이라면 제곱수가 없다는 뜻
if sumV >= 1:
    print(sumV)
    print(min(min_lst))
else:
    print('-1')