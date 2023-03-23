import sys
sys.stdin = open('input.txt', 'r')

def back_track(i, sumT):
    global ans
    if i >= N:           # nums 의 인덱스를 벗어나는 조건에서 리턴으로 빠져나옴
        return
    sumT += nums[i]
    if sumT == S:
        ans += 1

    back_track(i+1, sumT)
    back_track(i+1, sumT-nums[i]) # 처음을 예시로 들면 -3부터 시작하는 수열로 넘어감


N, S = map(int, input().split())

nums = list(map(int, input().split()))

ans = 0
back_track(0, 0)
print(ans)
