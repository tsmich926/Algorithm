for tc in range(4):
    x, y, p, q, x2, y2, p2, q2 = map(int, input().split())

    if q < y2 or x > p2 or y > q2 or x2 > p:    # 꼭짓점의 좌표가 다른직사각형보다 멀때
        print('d')

    elif (p == x2 and q == y2) or (x == p2 and q == y2) or (p == x2 and y == q2) or (x == p2 and y == q2):    # 꼭짓점이 맞닿아 있을때
        print('c')

    elif q == y2 or y == q2 or p == x2 or x == p2:    # 위의 조건에 만족하지 않는데 가로나 세로가 같을 때
        print('b')

    else:    # 그 외는 서로 포함되어 있는 것!
        print('a') 