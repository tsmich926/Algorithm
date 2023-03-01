R, C = map(int, input().split())

lst = [list(input()) for _ in range(R)]
word = []


# 가로보기
for i in range(R):
    tmp = ''
    for j in range(C):
        if lst[i][j] == '#':
            word.append(tmp)
            tmp = ''
            continue
        tmp += lst[i][j]
    word.append(tmp)




# 세로보기
for j in range(C):
    tmp = ''
    for i in range(R):
        if lst[i][j] == '#':
            word.append(tmp)
            tmp = ''
            continue
        tmp += lst[i][j]
    word.append(tmp)


word = sorted(word)
for i in word:
    if len(i) > 1:
        print(i)
        break