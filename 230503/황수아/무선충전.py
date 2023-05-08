def dfs(depth, targets, choice, num_BC):
    global max_power
    # print(choice)
    if depth >= 2:
        power = 0
        for i in range(len(choice)):
            if choice[i] == -1:
                continue
            ch = choice[i]
            power += BC[ch][-1] // num_BC[ch]
        # for i in range(len(num_BC)):
        #     if num_BC[i] > 0:
        #         power += num_BC[i]

        max_power = max(max_power, power)
        return

    if len(targets[depth]) > 0:





T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    users = []
    for _ in range(2):
        users.append(list(map(int, input().split())))
    BC = []
    for _ in range(A):
        x, y, c, p = list(map(int, input().split()))
        BC.append([y-1, x-1, c, p])

    field = [[[] for _ in range(10)] for _ in range(10)]

    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    for i in range(len(BC)):
        x, y, C = BC[i][:3]
        for j in range(0, C):
            nx = x - (C-j)
            if nx < 0 or nx >= 10:
                continue
            for k in range(-j, j+1):
                ny = y + k
                if ny < 0 or ny >= 10:
                    continue
                field[nx][ny].append(i)
    
        for j in range(C-1, -1, -1):
            nx = x + (C-j)
            if nx < 0 or nx >= 10:
                continue
            for k in range(-j, j+1):
                ny = y + k
                if ny < 0 or ny >= 10:
                    continue
                field[nx][ny].append(i)








    print(f"#{test_case} {}")