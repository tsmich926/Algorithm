def selection_sort(arr, k):
    for i in range(k):
        minidx = i
        for j in range(i+1, len(arr)):
            if arr[minidx] < arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr[k-1]
TC = int(input())
k = 3
for tc in range(1, TC+1):
    arr = list(map(int, input().split()))
    ans = selection_sort(arr, k)
    print(ans)