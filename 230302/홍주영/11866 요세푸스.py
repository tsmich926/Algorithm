import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

def per(K, d):
    ST = []
    ST.append(lis.pop(d))  # 처음 값을 pop 해주고 스택에 추가
    while lis:
        length = len(lis)
        if length == 1:            # 리스트 길이가 1이되면 스택에 추가하면서 반복문 탈출
            ST.append(lis.pop(0))
            break
        else:
            d = (d+K-1) % length      # d 증가시키면서
            ST.append(lis.pop(d))     # 스택에 추가
            if d >= length:           # d가 length 보다 길다면
                d = 0                 # d = 0 으로 바꿔줌
    return ST


lis = []
for i in range(1, N+1):
    lis.append(i)

d = K-1
a = str(per(K, d))            # 출력 형식에 맞게 바꿔줌
ans = a.replace('[', '<')
ans = ans.replace(']', '>')
print(ans)