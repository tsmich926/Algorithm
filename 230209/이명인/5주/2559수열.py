N, M = map(int, input().split())
arr = list(map(int, input().split()))
res = []
res.append(sum(arr[:M]))
for i in range(N-M):
    res.append(res[i] - arr[i] + arr[i+M])
print(max(res))