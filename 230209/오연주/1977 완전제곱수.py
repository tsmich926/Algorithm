# 완전제곱수 넣을 리스트 생성
square_lst = []

# 리스트에 완전제곱수를 넣어줌
for i in range(1, 101):
    square_lst.append(i**2)

# 입력값 입력
M = int(input())
N = int(input())

# 완전제곱수의 합의 초기값, 완전제곱수를 넣어줄 리스트를 만들어줌
squ_sum = 0
squ_lst = []

# 완전제곱수 리스트를 돌며 사이에 있는 i들을 구해줌
for i in square_lst:
    if M <= i <= N:
        squ_sum += i
        squ_lst.append(i)

# 완전제곱수 리스트에 요소가 있으면 합과 리스트의 첫번째 값 출력
if len(squ_lst) >= 1:
    print(f'{squ_sum}\n{squ_lst[0]}')
# 없으면 -1 출력
else:
    print(-1)