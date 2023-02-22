T = int(input())
for tc in range(T):
    ARR = list(map(int, input().split()))
    for i in range(9, 0, -1):    # 버블 정렬 사용
        for j in range(i):
            if ARR[j] > ARR[j+1]:
                ARR[j], ARR[j+1] = ARR[j+1], ARR[j]
    print(ARR[-3]) # 3번째로 큰 수