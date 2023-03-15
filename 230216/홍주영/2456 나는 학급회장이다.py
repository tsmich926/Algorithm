'''
N명의 학생
3명이 회장후보, N명의 학생들에게 선호도를 적어 내게 함
3점, 2점, 1점 순. 한번씩만 가능
만약 동률이면 3점이 더 많은 사람이 회장. 아니면 2점. 2점도 동률이면 결정X

정렬을 할 때, lambda를 활용하면 쉽게 풀 수 있음
'''

import sys
sys.stdin = open('input.txt', 'r')

방법1. 람다와 열거 사용
# vote = [[i] + [0]*3 for i in range(1, 4)]           # vote 에 첫 번째 index 에 후보 번호를 지정 해주고 0으로된 리스트 3개 생성
# N = int(input())
# for _ in range(N):                                  # 입력의 길이 만큼 돌면서
#     point = list(map(int, input().split()))         # 점수 가져옴
#     for idx, p in enumerate(point):                 # index 와 p(point[0, 1, 2] 순으로 반복) 를 반복 0 3/ 1 1 /2 2
#         vote[idx][p] += p                           # 맨 처음 생성한 vote 의 3개 공간의 index 가 점수고, 값이 합이 됨
# vote.sort(key=lambda x: (-sum(x[1:]), -x[3], -x[2]))  # 람다식을 사용하여 정렬하는데, 조건을 3가지를 설정 (앞의 -는 내림차순의미)
# if vote[0][1:] == vote[1][1:]:                      # 정렬한 뒤에 큰 값부터 정렬되는데 만약 1, 2, 3 자리가 모두 같다면
#     print(f'0 {sum(vote[0][1:])}')                  # 0을 리턴
# else:
#     print(f'{vote[0][0]} {sum(vote[0][1:])}')       # 아니면 후보의 번호와 각 자리수의 합을 리턴


# 방법2. pseudo code 대로 진행

N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
sum_lis = [0]*3                                      # sum 을 해줄 리스트 생성
cnt_list = [[0]*4 for _ in range(3)]                 # 각 후보마다 점수의 개수를 넣어줄 2차원배열 생성
for i in range(N):
    for j in range(3):
        sum_lis[j] += score[i][j]                    # 각 점수를 합해주고
        cnt_list[j][score[i][j]] += 1                # 카운팅 해줌
sum_max = max(sum_lis)                               # sum_lis 에서 가장 큰값을 sum_max 로 정의

nums = []                                            # 최대값이 여러개일 떄 넣어줄 리스트
for cd in range(3):
    if sum_lis[cd] == sum_max:                       # sum_lis 에서 그 값이 최대값이면 nums 에 넣어줌
        nums.append(cd)

cnt_list_t = list(zip(*cnt_list))                    # 계산하기 편하게 하기 위해 zip 으로 가로세로 돌려줌

cnt = 0
if len(nums) == 1:                                   # 만약 nums 의 길이가 1이면 최대값이 1개이기 때문에
    print(f'{nums[0]+1} {sum_max}')                  # 출력
else:
    for a in range(3, 1, -1):                        # nums 의 길이가 1이 아니면
        for b in range(3):
            cnt_max = max(cnt_list_t[a][:])          # cnt_list_t 의 끝줄(점수 3의 개수) 의 최대값을 설정해주고
            if cnt_list_t[a][b] == cnt_max:          # 그 줄을 돌면서 최대값이면(3의 개수가 가장 많으면)
                cnt += 1                             # 카운트 해주고 인덱스값(후보번호-1)을 저장
                num = b
        if cnt == 1:                                 # 만약 최대값이 1개이면
            print(f'{num+1} {sum_max}')              # 출력해주면서 종료
            break
    else:                                            # 3과 2의 최대값 카운트가 1이아니면
        print(f'0 {sum_max}')                        # 0과 최대값을 출력

