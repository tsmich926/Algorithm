for _ in range(int(input())):
    n = int(input())
    timbers = sorted(list(map(int, input().split())))
    level = 0
    for i in range(2,n):
        level = max(level, abs(timbers[i]-timbers[i-2]))
    print(level)