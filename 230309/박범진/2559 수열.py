import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
sumV = sum(arr[0:K])
maxV = sum(arr[0:K])

for i in range(K, N):
    sumV = sumV + arr[i] - arr[i-K]
    maxV = max(maxV, sumV)
print(maxV)