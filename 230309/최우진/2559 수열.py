N, K = map(int, input().split())
arr = list(map(int, input().split()))

first_sum = sum(arr[:K])
maxV = first_sum

for i in range(0, len(arr)-K):
    first_sum = first_sum - arr[i] + arr[i+K]
    if maxV < first_sum:
        maxV = first_sum

print(maxV)