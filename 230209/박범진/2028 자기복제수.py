# 1. 숫자를 제곱
# 2. 제곱한 숫자의 마지막 숫자(입력한 숫자의 길이만큼)를 숫자와 비교
T = int(input())
for tc in range(T):
    N = int(input())
    square = str(N ** 2)
    len_N = len(str(N))
    len_square = len(str(square))
    minus = len_square - len_N # 맨 끝에서 부터 minus까지 숫자를 비교
    rsq = square[len_square:minus-1:-1]
    real = rsq[::-1] # 뒤집으면 끝
    if real == str(N) or N == 1:
        print('YES')
    else:
        print('NO')