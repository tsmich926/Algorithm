N = int(input())
time = []


for i in range(N):
    s, e = list(map(int, input().split()))
    time.append([s, e])


time = sorted(time, key = lambda a : a[0]) # start 기준으로 오름차순 정렬
time = sorted(time, key = lambda a : a[1]) # end 기준으로 오름차순 정렬

# time = sorted(time, key = lambda a : (a[0], a[1]))  # 이것도 가능

# print(time)

last_end = 0
cnt = 0

for start, end in time:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)