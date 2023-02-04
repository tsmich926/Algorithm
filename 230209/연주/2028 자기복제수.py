# 자기복제수가 들어있는 리스트 만들기
num_list = []
for num in range(1, 1000 + 1): # N의 범위 1~ 1000까지
    self_num = num ** 2 # 자기복제수 정의
    # 슬라이싱 할 수 있게 문자열로 변형 후 num의 길이만큼 self_num의 뒷부분 자름
    if str(num) in str(self_num)[len(str(self_num))-len(str(num)):]:
        num_list.append(num) # num_list에 자기복제수 추가

# 테스트 케이스 입력 부분
T = int(input())
for tc in range(1, T + 1):
    nums = int(input()) # 문자열 입력을 숫자로
    if nums in num_list: # 리스트에 있으면 YES 없으면 NO
        print('YES')
    else:
        print('NO')