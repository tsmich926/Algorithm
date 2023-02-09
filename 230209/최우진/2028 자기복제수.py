TC = int(input())   # testcase 입력 
for tc in range(TC):
    num = int(input())  # 입력값
    num_s = str(num)    # 입력값 문자열로 바꿔줌(뒤에서 문자열 슬라이싱 작업 위해)

    nums = num**2  # 입력값 제곱
    nums_s = str(nums)  # 제곱한 입력값 문자열로 바꿔줌(뒤에서 문자열 슬라이싱 작업을 위해)

    if int(nums_s[-len(num_s):]) == num:   
        print('YES')
    else:
        print('NO')
# 문자열로 바꿔준 제곱값의 뒤에서 부터 원래 입력값의 길이 만큼 추출한 값을 int형으로 바꿔줬을 때 
# 입력값과 같으면 YES 프린트하고 입력값과 다르면 NO 프린트