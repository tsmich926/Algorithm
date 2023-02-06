'''
일곱난쟁이
의자 7 접시 7 나이프 7

아홉난쟁이가 돌아옴
난쟁이모자에 100보다 작은 양의 정수
일곱난쟁이의 모자의 숫자의 합이 100
일곱난쟁이를 찾는 프로그램 작성
부분집합으로 풀기
'''


import sys
sys.stdin = open('input.txt', 'r')

def my_sum(lis):
    sumV = 0
    for i in lis:
        sumV += i
    return sumV

lis = []
for _ in range(9):
    N = int(input())
    lis.append(N)
for i in range(1<<len(lis)):
    subset = []
    for j in range(len(lis)):
        if i & (1 << j):
            subset.append(lis[j])
    if len(subset) == 7 and my_sum(subset) == 100:
        for k in range(7):
            print(subset[k])
