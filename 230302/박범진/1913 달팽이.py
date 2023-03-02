N = int(input())
P = int(input())
ARR = [[0] * N for _ in range(N)]

#    아래 오른 위 왼
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
row = 0
col = 0
d = 0
find_row = -1    # 정답좌표라서 그냥 절대 나오지 않는 숫자 -1을 사용
find_col = -1
for i in range(N*N, 0, -1):    # 0,0을 제일 큰 수부터 시작해서 아래, 오른, 위, 왼쪽의 순서로 돌게하기
    ARR[row][col] = i
    if ARR[row][col] == P:
        find_row = row
        find_col = col
    newR = row + dr[d]
    newC = col + dc[d]
    if newR < 0 or newC < 0 or newR >= N or newC >= N or ARR[newR][newC] != 0:    # 방향을 조절
        d = (d+1) % 4
    row = row + dr[d]
    col = col + dc[d]

for num in ARR:
    print(*num)
print(find_row+1, find_col+1)