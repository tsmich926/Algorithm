N,K = map(int,input().split())
degree = list(map(int,input().split()))
ans = ssum = sum(degree[:K])
for i in range(K,N):
    ssum = ssum+degree[i]-degree[i-K]
    ans = max(ans,ssum)
print(ans)