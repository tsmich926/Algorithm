# 9개 중 랜덤으로 7개를 뽑기 위해 랜덤 모듈 사용
import random

# 9개의 숫자가 하나씩 입력되기 때문에 입력을 9번 반복하여 nums 리스트에 추가
nums = []
for i in range(9):
    num = int(input())
    nums.append(num)

# 랜덤 모듈을 사용해서 7개를 뽑아 합이 100이 될때까지 반복문을 돌림
while True: # 무한 반복
    nums_lst = random.sample(nums, 7)
    numsum = 0
    for i in nums_lst:
        numsum += i
    # 반복문의 합이 100이 되면 반복 종료
    if numsum == 100:
        break

# random.sample은 순서 상관없이 숫자를 뽑기 때문에 버블 정렬을 이용하여 오름차순으로 정렬
# 길이보다 인덱스는 1이 작기 때문에 빼줌, 1번 인덱스까지 정렬되면 첫번째 인덱스는 정렬할 필요가 없기 때문에 0은 포함 안 함
# 맨 뒤부터 정렬되기 때문에 반대로
for i in range(len(nums_lst)-1, 0, -1):
    # 첫번째 두번째, 두번째 세번째... 순서대로 정렬해서 자리 바꿈
    for j in range(i):
        if nums_lst[j] > nums_lst[j+1]:
            nums_lst[j], nums_lst[j+1] = nums_lst[j+1], nums_lst[j]

# 숫자만 출력, sep= 숫자 사이사이 어떤 걸 넣어 출력하는지
print(*nums_lst, sep='\n')

