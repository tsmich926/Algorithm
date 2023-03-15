R, C = map(int, input().split())
ARR = [list(input())+['#'] for _ in range(R)] + [['#'] * (C+1)]    # 오른쪽과 아래에 out of index를 피하게 해줄 보험 #을 한줄씩 깔아주기
new_ARR = list(map(list, zip(*ARR)))    # 가로와 세로를 바꾼 배열
ans = []    
res = []
for i in range(R):
    j = 0
    while j < len(ARR[i]):
        if ARR[i][j].isalpha() and ARR[i][j+1].isalpha():    # 첫번째 문자와 그다음 문자가 둘다 알파벳이면
            ARR[i][j] = ARR[i][j] + ARR[i][j+1]    # 그 두 문자를 더하고 
            ARR[i].pop(j+1)    # 두번째 문자 제거
            continue
        else:    # 두번째 문자가 알파벳이 아닌 '#'이면
            ans.append(ARR[i][j])    # 문자를 정답리스트에 추가
            j += 1

for i in range(C):    # 세로도 마찬가지로 반복
    j = 0
    while j < len(new_ARR[i]):
        if new_ARR[i][j].isalpha() and new_ARR[i][j+1].isalpha():
            new_ARR[i][j] = new_ARR[i][j] + new_ARR[i][j+1]
            new_ARR[i].pop(j+1)
            continue
        else:
            ans.append(new_ARR[i][j])
            j += 1

for i in ans:    # 이러면 정답리스트에 정답문자들과 길이가 한글자인 알파벳문자들이 남는데
    if len(i) > 1:    # 길이가 한글자 이상인 문자중에서 정답문자를 찾으면 끝
        res.append(i)
print(sorted(res)[0])