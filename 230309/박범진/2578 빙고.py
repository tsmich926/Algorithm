def bingo_check(count):
    bingo_check_count = 0
    if count[0][0] == 1 and count[1][1] == 1 and count[2][2] == 1 and count[3][3] == 1 and count[4][4] == 1:
        bingo_check_count += 1

    if count[0][4] == 1 and count[1][3] == 1 and count[2][2] == 1 and count[3][1] == 1 and count[4][0] == 1:
        bingo_check_count += 1

    for i in range(5):
        if count[i][0] == 1 and count[i][1] == 1 and count[i][2] == 1 and count[i][3] == 1 and count[i][4] == 1:
            bingo_check_count += 1

        if count[0][i] == 1 and count[1][i] == 1 and count[2][i] == 1 and count[3][i] == 1 and count[4][i] == 1:
            bingo_check_count += 1

        if bingo_check_count == 3:
            return 'bingo'



def count_check(bingo, arr, count):
    countV = 0
    for i in range(5):
        for j in range(5):
            num = bingo[i][j]

            for k in range(5):
                for l in range(5):
                    if arr[k][l] == num:
                        count[k][l] += 1
                        countV += 1

                        if bingo_check(count) == 'bingo':
                            return countV


arr = [list(map(int, input().split())) for _ in range(0, 5)]
bingo = [list(map(int, input().split())) for _ in range(5, 10)]
count = [[0]*5 for _ in range(5)]

print(count_check(bingo, arr, count))