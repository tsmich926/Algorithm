# 1. 인접한 옆 통나무로 건너뛰는데 인접한 통나무의 높이 차가 최소가 되야한다는 것은 편차가 들쭉날쭉 하다는게 아니라 고르게 편성되어야 한다는 것
# 2. 인접한 옆이므로 양옆을 검사해 줘야함
# 3. 가장 높은 통나무를 가운데에, 두번째 세번째 높은 통나무를 양옆에 그 각각의 옆에 네번째 다섯번째 이런식으로 배치했음
# 4. 결국 내림차순으로 정렬한 후 2개씩 검사하면서 가장 높이의 차가 큰 값을 찾으면 끝


T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    ans = 0
    for i in range(0, N-2):
        if lst[i] - lst[i+1] > ans:    # 제일 큰 통나무에서 두번째로 큰 통나무의 높이의 차
            ans = lst[i] - lst[i+1]
        if lst[i] - lst[i+2] > ans:    # 제일 큰 통나무에서 세번째로 큰 통나무의 높이의 차
            ans = lst[i] - lst[i+2]
    print(ans)