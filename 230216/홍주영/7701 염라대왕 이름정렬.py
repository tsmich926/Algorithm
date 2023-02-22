'''
염라대왕의 이름 정렬
길이가 긴 문자열은 아래로, 짧은 문자열은 위로
문자열의 첫번째 자리부터 비교하며 사전순 정렬( sort()활용)
문자열의 길이가 같을 때,
'''


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(set([input() for _ in range(N)]))        # 입력값을 set()을 이용해 중복을 제거하고 list()로 다시 리스트화 해줌
    arr.sort(key=lambda x: (len(x),x))                  # sort() 메서드는 사전 순으로 정렬하는데
    print(f'#{tc}')                                     # 람다조건을 넣어서 길이를 우선순위로 정렬한 후, 사전 순으로 정렬
    for i in arr:                                       # 리스트를 돌면서 출력
        print(i)
