import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 1. 버블소트로 내림차순 정렬해줌
# for tc in range(1, T+1):
#     A = list(map(int, input().split()))
#     for i in range(9, 0, -1):
#         for j in range(0, i):
#             if A[j] < A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]


# 첫번째 예제로 예를들면
# A = [1000, 9, 8, 7, 6, 5, 4, 3, 2, 1] 로 정렬이 된다.
#     print(A[2])

# 2. 람다를 이용해 정렬

# for tc in range(1, T+1):
#     A = list(map(int, input().split()))
#     A = sorted(A, key= lambda x : -x)
#     print(A[2])

# 3. 셀렉션 알고리즘

# for tc in range(1, T+1):
#     A = list(map(int, input().split()))
#     for i in range(9):
#         maxIdx = i
#         for j in range(i+1, 10):
#             if A[maxIdx] < A[j]:
#                 maxIdx = j
#         A[i], A[maxIdx] = A[maxIdx], A[i]
#     print(A[2])