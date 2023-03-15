R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
wword = []

# 반복문을 통해 가로로 연속되는 단어를 찾는다.
for i in range(R):
    word = ""
    for j in range(C):
        # 현재 문자가 # 아니면 문자를 낱말에 더해준다.
        if arr[i][j] != "#":
            word += arr[i][j]

        # 현재 문자가 # 이면서 낱말의 길이가 2이상이면 낱말모음에 추가한다.
        elif len(word) >= 2:
            wword.append(word)

        # 현재 문자가 # 이면서 낱말의 길이가 2 미만이라면 필요없는? 낱말이므로 "" 초기화화
        else:
            word = ""

    if len(word) >= 2:
        wword.append(word)


# 반복문을 통해 세로로 연속되는 단어를 찾는다.
for i in range(C):
    word = ""
    for j in range(R):
        if arr[j][i] != "#":
            word += arr[j][i]
        elif len(word) >= 2:
            wword.append(word)
        else:
            word = ""

    if len(word) >= 2:
        wword.append(word)

# 사전식 순으로 정렬 후 첫 번째 낱말을 출력
word.sort()
print(word[0])