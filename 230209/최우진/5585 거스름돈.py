cost = int(input())
rest = 1000 - cost

cnt = 0
while rest != 0:
    if rest >= 500:
        cnt += 1
        rest = rest - 500
    elif rest >= 100 and rest < 500:
        a = rest//100
        cnt = cnt + a
        rest = rest - (100*a)
    elif rest >= 50 and rest < 100:
        b = rest // 50
        cnt = cnt + b
        rest = rest - (50 * b)
    elif rest >= 10 and rest < 50:
        c = rest // 10
        cnt = cnt + c
        rest = rest - (10 * c)
    elif rest >= 5 and rest < 10:
        d = rest // 5
        cnt = cnt + d
        rest = rest - (5 * d)
    elif rest >= 0 and rest < 5:
        e = rest // 1
        cnt = cnt + e
        rest = rest - e

print(cnt)