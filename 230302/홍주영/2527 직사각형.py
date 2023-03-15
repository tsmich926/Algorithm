import sys
sys.stdin = open('input.txt', 'r')

def func():
    if x2 == x3 or x1 == x4:
        if y1 == y4 or y2 == y3:
            return 'c'   # 점
        else:
            if (y3 < y2 and y4 > y1) or (y1 < y4 and y2 > y3):
                return 'b'   # 선분
            else:
                return 'd'
    elif y1 == y4 or y2 == y3:
        if (x3 < x2 and x4 > x1) or (x1 < x4 and x2 > x3):
            return 'b'      # 선분
        else:
            return 'd'

    # 직사각형
    if x1 <= x3 < x2 and x2 < x4:
        if y3 < y2 and y4 > y1:
            return 'a'
    if x1 <= x3 < x2 and x1 < x4 <= x2:
        if y1 < y4 and y3 < y2:
            return 'a'
    if x3 <= x1 < x4 and x3 < x2 <= x4:
        if y3 < y2 and y1 < y4:
            return 'a'
    if x3 <= x1 < x4 and x4 < x2:
        if y1 < y4 and y2 > y3:
            return 'a'
    # 모두가 아니면 안겹침
    return 'd'




for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    print(func())
