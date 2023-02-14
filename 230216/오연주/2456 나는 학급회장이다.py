T = int(input())

sumA = [0] * 4
sumB = [0] * 4
sumC = [0] * 4
for tc in range(T):
    A, B, C = map(int, input().split())
    sumA[A]