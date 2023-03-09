def bingo_check(count):
    bingo_check_count = 0    # 빙고가 3개가 되면 '빙고!'
    if count[0][0] == 1 and count[1][1] == 1 and count[2][2] == 1 and count[3][3] == 1 and count[4][4] == 1:        # 오른쪽으로 대각선이 빙고면
        bingo_check_count += 1

    if count[0][4] == 1 and count[1][3] == 1 and count[2][2] == 1 and count[3][1] == 1 and count[4][0] == 1:        # 왼쪽으로 대각선이 빙고면
        bingo_check_count += 1

    for i in range(5):
        if count[i][0] == 1 and count[i][1] == 1 and count[i][2] == 1 and count[i][3] == 1 and count[i][4] == 1:    # 가로가 빙고면
            bingo_check_count += 1

        if count[0][i] == 1 and count[1][i] == 1 and count[2][i] == 1 and count[3][i] == 1 and count[4][i] == 1:    # 세로가 빙고면
            bingo_check_count += 1

        if bingo_check_count == 3:
            return 'bingo'

def count_check(bingo, arr, count):
    countV = 0
    for i in range(5):
        for j in range(5):
            num = bingo[i][j]            # 먼저 빙고 리스트의 숫자를 차례대로 저장

            for k in range(5):
                for l in range(5):
                    if arr[k][l] == num:  # arr리스트에서 그 숫자를 찾으면
                        count[k][l] += 1  # 카운트 리스트에 똑같은 인덱스에 1을 더하고
                        countV += 1       # 몇 번째에 찾았는지 알기 위해 한번에 1씩 더함

                        if bingo_check(count) == 'bingo':
                            return countV


arr = [list(map(int, input().split())) for _ in range(0, 5)]
bingo = [list(map(int, input().split())) for _ in range(5, 10)]
count = [[0]*5 for _ in range(5)]         # 카운트리스트에 1씩 더하는 식으로 빙고를 찾기

print(count_check(bingo, arr, count))