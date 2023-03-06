R, C = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr, dc = map(int, input().split())

sumV = 0
for i in arr:
    if dr == i[0]:
        sumV += abs(dc-i[1])

    elif (dr == 1 and i[0] == 2) or (dr == 2 and i[0] == 1):
        sum1 = dc + C + i[1]
        sum2 = (R-dc) + C + (R-i[1])
        if sum1 < sum2:
            sumV += sum1
        else:
            sumV += sum2

    elif (dr == 3 and i[0] == 4) or (dr == 4 and i[0] == 3):
        sum1 = dc + R + i[1]
        sum2 = (C - dc) + R + (C - i[1])
        if sum1 < sum2:
            sumV += sum1
        else:
            sumV += sum2

    elif (dr == 1 and i[0] == 3) or (dr == 3 and i[0] == 1):
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