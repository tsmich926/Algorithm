T = int(input())
paper = [[0] * 101 for _ in range(101)]

for _ in range(T):
    n1, n2 = map(int, input().split())
    for i in range(n1, n1+10):
        for j in range(n2, n2+10):
            paper[i][j] = 1

cnt = 0
for i in range(len(paper)):
    for j in range(len(paper)):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)
