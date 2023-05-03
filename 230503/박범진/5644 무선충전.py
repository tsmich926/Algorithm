from collections import deque


# 1. 배터리 충전소의 범위를 구해 board에 저장하자!

def BFS(num, si, sj, coverage):
    visited = [[False] * 10 for _ in range(10)]
    Queue = deque()
    Queue.append((si, sj))
    visited[si][sj] = True
    board[si][sj].append(num)
    for _ in range(coverage):
        for _ in range(len(Queue)):
            ci, cj = Queue.popleft()
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < 10 and 0 <= nj < 10 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    Queue.append((ni, nj))
                    board[ni][nj].append(num)


# 2. 한칸씩 이동하면서 배터리 충전소의 여부를 체크하자!

def move():
    ai, aj, bi, bj = 0, 0, 9, 9
    check(ai, aj, bi, bj)
    i = 0
    while i < Move_Count:
        a = A_move.popleft()
        b = B_move.popleft()
        ai += Direction[a][0]
        aj += Direction[a][1]
        bi += Direction[b][0]
        bj += Direction[b][1]
        check(ai, aj, bi, bj)
        i += 1


# 3. 배터리 충전소의 경우에 수에 따라 체크!

def check(ai, aj, bi, bj):
    global ans
    a = board[ai][aj]
    b = board[bi][bj]
    if not a and b:    # 1. a는 배터리 충전소에 없고 b는 배터리 충전소에 있을 때
        maxV = 0
        for num in b:
            if power[num] > maxV:
                maxV = power[num]
        ans += maxV
        return

    elif a and not b:  # 2. a는 배터리 충전소에 있고 b는 배터리 충전소에 없을 때
        maxV = 0
        for num in a:
            if power[num] > maxV:
                maxV = power[num]
        ans += maxV
        return

    elif a and b:    # 3. a와 b모두 배터리 충전소에 있을 때
        sumV = 0
        for i in a:
            for j in b:
                if i == j:    # 3-1. 둘이 같은 충전소에 있으면 둘의 충전 양을 더하지 않고 한명의 충전양만 보낸다.
                    if power[i] > sumV:
                        sumV = power[i]
                else:         # 3-2. 둘이 다른 충전소에 있으면 각각의 충전소양을 더한 충전양을 보낸다
                    suma = power[i]
                    sumb = power[j]
                    if suma + sumb > sumV:
                        sumV = suma + sumb

        ans += sumV
        return



        #     제자리     상       우      하       좌
Direction = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    power = {}
    ans = 0
    board = [[[] for _ in range(10)] for _ in range(10)]
    Move_Count, BC_Count = map(int, input().split())
    A_move = deque(list(map(int, input().split())))
    B_move = deque(list(map(int, input().split())))

    for num in range(1, BC_Count + 1):
        y, x, coverage, performance = map(int, input().split())   # y, x가 거꾸로 되어있음
        power[num] = performance
        BFS(num, x-1, y-1, coverage)
    move()
    print(f'#{tc} {ans}')