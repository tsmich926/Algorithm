N, K = map(int, input().split())
lst = list(map(int, input().split()))

window = sum(lst[:K])
answer = window
for i in range(K, N):
    window += lst[i] - lst[i-K]
    answer = max(answer, window)
print(answer)