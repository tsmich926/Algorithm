N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))
lis = [[]]
# print(len(lis))

# 부분집합 만들어주기
for num in arr:
  size = len(lis)
  for y in range(size):
    lis.append(lis[y]+[num])
    # print(lis)

ans_lis = lis[1:] #공집합 제거
# print(ans_lis)

cnt = 0
for i in ans_lis:
  if sum(i) == S:
    cnt += 1
print(cnt)