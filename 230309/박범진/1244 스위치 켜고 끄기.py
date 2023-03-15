# 어렵게 접근한 방법
# 성별이 남자일때는 문제가 안됨.
# 성별이 여자일때:
# 조건을 만족할때마다 1씩 더함. 그래서 마지막에 홀수이면 켜져있고 짝수이면 꺼져있다는 뜻

L = int(input())
arr = list(map(int, input().split()))
M = int(input())
for i in range(M):
    S, N = map(int, input().split())
    if S == 1:                            # 성별이 남자이고
        for j in range(1, L+1):
            if j % N == 0:
                if arr[j-1] == 0:         # 스위치가 꺼져있으면
                    arr[j-1] += 1         # 1을 더해주고
                else:                     # 스위치가 켜져있으면
                    arr[j-1] -= 1         # 1을 빼준다

    if S == 2:                            # 성별이 여자일때
        arr[N-1] += 1                     # 처음에 일단 스위치를 누르고 시작
        tmp1 = N-1
        tmp2 = N-1
        while tmp1 > 0 and tmp2 < L-1:    # 인덱스를 벗어나면 종료
            tmp1 -= 1                     # 스위치를 누른곳 부터 왼쪽으로 한칸씩
            tmp2 += 1                     # 스위치를 누른곳에 오른쪽으로 한칸씩
            if arr[tmp1] == arr[tmp2]:    # 대칭의 스위치 상태가 같으면
                arr[tmp1] += 1            # 스위치를 누르기
                arr[tmp2] += 1            # 스위치를 누르기
            else:
                break

    for i in range(L):                    # 마지막에 홀수 짝수를 판단해 스위치 리스트 다시 정렬
        if arr[i] % 2 == 0:
            arr[i] = 0
        else:
            arr[i] = 1

for i in range(0, L, 20):
    print(*arr[i:i+20])









# 두번째
# 그냥 함수를 만들어서 켜져있는지 꺼져있는지 보고 바꿔주면 됨
def turn(n):
    if arr[n] == 0:
        arr[n] = 1
    else:
        arr[n] = 0
    return


L = int(input())
arr = list(map(int, input().split()))
M = int(input())
for i in range(M):
    S, N = map(int, input().split())
    if S == 1:
        for j in range(1, L+1):
            if j % N == 0:
                turn(j-1)     # 조건에 만족시 함수 실행

    if S == 2:
        turn(N-1)
        tmp1 = N-1
        tmp2 = N-1
        while tmp1 > 0 and tmp2 < L-1:
            tmp1 -= 1
            tmp2 += 1
            if arr[tmp1] == arr[tmp2]:
                turn(tmp1)    # 조건에 만족시 함수 실행
                turn(tmp2)    # 조건에 만족시 함수 실행
            else:
                break

for i in range(0, L, 20):
    print(*arr[i:i+20])