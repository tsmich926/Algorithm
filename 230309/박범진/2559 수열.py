import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
sumV = sum(arr[0:K])
maxV = sum(arr[0:K])

for i in range(K, N):
    sumV = sumV + arr[i] - arr[i-K]    # 맨 앞의 수를 빼고 맨 뒤에수를 더하는 식으로 계속 비교
    maxV = max(maxV, sumV)
print(maxV)