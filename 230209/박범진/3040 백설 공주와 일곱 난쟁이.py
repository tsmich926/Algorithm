def seven(arr, sumV):
    for i in range(0, 8):
        for j in range(i+1, 9):
            if arr[i] + arr[j] == sumV - 100:
                f_lst.append(arr[i])
                f_lst.append(arr[j])
                return

arr = [int(input()) for _ in range(9)]
sumV = sum(arr)
f_lst = []
ans = []

seven(arr, sumV)

for i in arr:
    if i not in f_lst:
        ans.append(i)
ans = sorted(ans)

for i in ans:
    print(i)