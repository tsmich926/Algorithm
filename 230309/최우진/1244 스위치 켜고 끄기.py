switch_N = int(input())
arr = list(map(int, input().split()))
student_N = int(input())

for _ in range(student_N):
    gender, start_N = list(map(int, input().split()))
    go = 0
    cnt = 0


    if gender == 1:
        for i in range(1, switch_N+1):
            if i % start_N == 0:
                if arr[i-1] == 0:
                    arr[i-1] = 1
                elif arr[i-1] == 1:
                    arr[i-1] = 0


    elif gender == 2:
        go += 1

        while True:
            if (start_N-1) - go >= 0 and (start_N-1) + go <= switch_N-1:
                if arr[(start_N-1) - go] == arr[(start_N-1) + go]:

                    cnt += 1
                    go += 1

                else:

                    break
            else:
                break

        if cnt >= 1:
            for i in range(start_N-1-cnt, start_N+cnt):
                if arr[i] == 0:
                    arr[i] = 1
                elif arr[i] == 1:
                    arr[i] = 0
        else:
            if arr[start_N-1] == 0:
                arr[start_N - 1] = 1
            else:
                arr[start_N - 1] = 0


for i in range(switch_N):
    if i % 20 == 0 and i > 0:
        print()
    print(arr[i], end = ' ')