def dfs(num, dir):
    # 방문표시 하는 이유 : 한번만 돌려주는것이기 때문
    result[num] = 1

    #1, 2는 맨 처음 양쪽 비교해야 함
    #0, 3은 처음엔 한쪽만 비교

    # 012라면
    if num < 3:
        if lst[num][2] != lst[num+1][6] and not result[num+1]:
            # 돌려준다
            dfs(num + 1, -1*dir)

    # 123이라면
    if num > 0:
        if lst[num][6] != lst[num-1][2] and not result[num-1]:
            # 돌려준다
            dfs(num - 1, -1*dir)


    if dir == 1:
        # 시계방향 : 12345678 > 81234567
        v = lst[num].pop(-1)
        lst[num].insert(0, v)
    else:
        # 반시계방향 : 12345678 > 23456781
        v = lst[num].pop(0)
        lst[num].append(v)



T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    lst = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        N, D = map(int, input().split())
        result = [0]*4
        dfs(N - 1, D)

    res = 0
    for i in range(4):
        res += lst[i][0]*2**i
    print(f'#{tc} {res}')



# 문제에서 톱니바퀴 돌릴 때 이미 돌린 상태에서 만나는 것을 비교하는게 아니라
# 하나가 돌아간다고 하면 나머지 2, 6번을 비교해서 돌리는 것


def check(num, dir):
    visited[num] = 1

    # 시계 방향으로 회전할 때
    if dir == 1:

        # 돌려야 할 톱니 다음 것이 있으면(0, 1, 2번)
        # 2번위치와 6번 비교해준다
        if 0<=num+1<=3 and not visited[num+1] and lst[num][2] != lst[num+1][6]:
            # 돌린것과 반대로 돌림
            check(num+1, -1)

        # 돌려야 할 톱니 이전 것이 있으면(1, 2, 3번)
        # 6번위치와 2번 비교해준다
        if 0<=num-1<=3 and not visited[num-1] and lst[num-1][2] != lst[num][6]:
            # 돌린것과 반대로 돌려줌
            check(num-1, -1)

        # 시계방향 : 12345678 > 81234567
        v = lst[num].pop(-1)
        lst[num].insert(0, v)

        # fig-2 : 0번 첫번째 if문 들어감 > 1번에서 첫번째 if문 : 이미 방문, 두번째 if문 : 서로 같아서 안됨
        # 1번 회전시키고 > 0번 회전시킴



    if dir == -1:
        # 돌려야 할 톱니 다음 것이 있으면(0, 1, 2번)
        # 2번위치와 6번을 비교해준다
        if 0<=num+1<=3 and not visited[num+1] and lst[num][2] != lst[num+1][6]:
            #돌린것과 반대로 돌려줌
            check(num+1, 1)

        # 돌려야 할 톱니 이전 것이 있으면(1, 2, 3번)
        # 6번위치와 2번 비교해준다
        if 0<=num-1<=3 and not visited[num-1] and lst[num-1][2] != lst[num][6]:
            # 돌린것과 반대로 돌려줌
            check(num-1, 1)

        # 반시계방향 : 12345678 > 23456781
        v = lst[num].pop(0)
        lst[num].append(v)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(N):
        n1, dir1 = map(int, input().split())
        visited = [0]*4
        check(n1-1, dir1)

    res = 0
    for i in range(4):
        res += lst[i][0] * 2**i

    print(f'#{tc} {res}')
