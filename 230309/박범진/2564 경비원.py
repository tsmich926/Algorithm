R, C = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = map(int, input().split())

sumV = 0
for i in arr:
    if dr == i[0]:              # 1. 동근이가 있는 동서남북의 위치와 상점의 동서남북 위치가 같을때
        sumV += abs(dc-i[1])    # 그냥 빼면 됨

    elif (dr == 1 and i[0] == 2) or (dr == 2 and i[0] == 1):    # 2. 블록이 마주보고 있는 경우
        sum1 = dc + C + i[1]                                    # 왼쪽으로 돌아가는 경우와
        sum2 = (R-dc) + C + (R-i[1])                            # 오른쪽으로 돌아가는 경우를 구해
        if sum1 < sum2:                                         # 비교하기
            sumV += sum1
        else:
            sumV += sum2

    elif (dr == 3 and i[0] == 4) or (dr == 4 and i[0] == 3):
        sum1 = dc + R + i[1]
        sum2 = (C-dc) + R + (C-i[1])
        if sum1 < sum2:
            sumV += sum1
        else:
            sumV += sum2

    elif (dr == 1 and i[0] == 3) or (dr == 3 and i[0] == 1):    # 3. 나머지 모든 경우를 일일이 구함
        sumV += (dc + i[1])
    elif dr == 1 and i[0] == 4:
        sumV += (R-dc) + i[1]
    elif dr == 4 and i[0] == 1:
        sumV += dc + (R-i[1])
    elif dr == 2 and i[0] == 3:
        sumV += dc + (C-i[1])
    elif dr == 3 and i[0] == 2:
        sumV += (C-dc) + i[1]
    elif dr == 2 and i[0] == 4:
        sumV += (R-dc) + (C-i[1])
    elif dr == 4 and i[0] == 2:
        sumV += (C-dc) + (R-i[1])

print(sumV)