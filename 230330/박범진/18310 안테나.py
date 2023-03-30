# 그냥 중간에 있는게 무슨 방법이든 가장 작은 결과를 낼 수 있음

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

a = 0
if N % 2 == 0:
    b = N//2
else:
    b = (N//2) + 1

print(arr[a-1])