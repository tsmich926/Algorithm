def seven(arr, sumV):
    for i in range(0, 8):
        for j in range(i+1, 9):
            if arr[i] + arr[j] == sumV - 100:    # 모든 난쟁이를 더한 값에서 100을 빼면 가짜 난쟁이 둘의 값이 나옴
                f_lst.append(arr[i])    # 가짜 난쟁이1 가짜리스트에 추가
                f_lst.append(arr[j])    # 가짜 난쟁이2 가짜 리스트에 추가
                return

arr = [int(input()) for _ in range(9)]
sumV = sum(arr)
f_lst = []
ans = []

seven(arr, sumV)

for i in arr:
    if i not in f_lst:    # 가짜 난쟁이 둘을 제외한 나머지 난쟁이들 정답 리스트에 추가
        ans.append(i)
ans = sorted(ans)

for i in ans:
    print(i)