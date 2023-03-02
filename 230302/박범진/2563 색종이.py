T = int(input())
ARR = []
New_arr = []
for _ in range(T):
    N, M = map(int, input().split())
    for i in range(M, M+10):     # 가로와 세로에 10씩 길이를 추가해서
        for j in range(N, N+10):
            ARR.append([i, j])    # ARR리스트에 더하기

for k in ARR:    
    if k not in New_arr:
        New_arr.append(k)    # 중복되는 좌표를 거르면 겹치지 않는 사각형의 넓이만 구할 수 있음

print(len(New_arr))