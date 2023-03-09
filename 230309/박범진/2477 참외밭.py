# 모든 참외밭은 가로로 가장 긴 변과 세로로 가장 긴 변이 존재하고 그 두 변은 붙어 있을 수 밖에 없음
# 그럼 가로로 가장 긴 변과 세로로 가장 긴 변을 곱한 사각형에서 나머지 빈 사각형을 구해서 빼면 됨

N = int(input())
ans = []
for _ in range(6):
    R, C = map(int, input().split())
    ans.append((R, C))

count = [0]*5
for i in ans:               # 방향이 몇개인지 확인
    count[i[0]] += 1

a = 0
b = 0
maxV = 0
for i in ans:                # 가로 혹은 세로중에 가장 긴 변 a
    if count[i[0]] == 1:
        if maxV < i[1]:
            a = i

tmp = ans[::]                # 리스트와 똑같은 임시리스트를 만들어서 가장 긴 변 a를 제거
for i in tmp:
    if i == a:
        tmp.remove(i)

maxV2 = 0                     # 세로 혹은 가로중에 가장 긴 변 b
for i in tmp:
    if count[i[0]] == 1:
        if maxV2 < i[1]:
            b = i

ans.insert(0, ans[5])         # out of index를 피하기 위해 리스트의 맨 앞에 리스트의 맨뒤에 있던 튜플을 더하고
ans.insert(7, ans[1])         # 리스트의 맨 뒤에 리스트의 맨 앞에 있던 튜플을 더함

c = 0
d = 0
for i in range(1, 7):
    if ans[i] == a and ans[i-1] != b:    # 가로 혹은 세로 중에 가장 긴 변을 구하고 맞닿아 있는 세로 혹은 가로 중에 가장 긴 변이 아닐 때
        c += ans[i-1][1]
    elif ans[i] == a and ans[i+1] != b:
        c += ans[i+1][1]
    if ans[i] == b and ans[i-1] != a:
        d += ans[i-1][1]
    elif ans[i] == b and ans[i+1] != a:
        d += ans[i+1][1]

res = (a[1]*b[1]) - ((a[1]-d) * (b[1]-c))
print(N*res)