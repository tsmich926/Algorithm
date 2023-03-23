import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
lis = []
for i in range(N):
    s, e = map(int, input().split())
    lis.append([s, e])

lis.sort(key=lambda x: [x[1], x[0]])  # lis 의 두번 째 값인 끝나는 시간부터 큰 순으로 먼저 정렬, 같으면 2번째 인자인 시작시간이 큰 순서로
                                      # 정렬

ans = 1
end_t = lis[0][1]
for j in range(1, N):
    if lis[j][0] >= end_t:
        ans += 1
        end_t = lis[j][1]

print(ans)