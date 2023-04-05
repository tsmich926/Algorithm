N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

arr_len = len(arr)
# print(arr[arr_len//2])

if arr_len % 2 == 1:
    print(arr[arr_len//2])
else:
    print(arr[arr_len//2-1])