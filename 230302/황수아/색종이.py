N = int(input()) #색종이 몇개 붙일건지
arr = [[0]*100 for _ in range(100)] #100X100 도화지 만들기
for i in range(N):
    G,S = map(int,input().split()) #색종이 붙이는 위치/옆/아래/
    #색종이가 붙은 영역을 표시
    for row in range(G,G+10):
        for col in range(S,S+10):
            arr[row][col] += 1


#100X100 형태의 도화지 검사작업
cnt = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] != 0: #안겹치는 부분은 1으로 표시되고 겹치는 부분은 2나 3.. 등으로 표시됨
            cnt += 1 #0인 부분만 빼고 카운트해준다
print(cnt)