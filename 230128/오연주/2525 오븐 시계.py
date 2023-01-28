a, b = map(int, input().split())
c = int(input())
d = c // 60 # c가 걸리는 시간
e = c % 60  # c가 걸리는 분

hour = a + d
minute = b + e
if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print(hour, minute)