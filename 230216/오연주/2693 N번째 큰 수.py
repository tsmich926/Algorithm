N = 3
T = int(input())

# 버블 정렬 이용
for i in range(T):
    A = list(map(int, input().split()))
    for i in range(len(A)-1, -1, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    print(A[-3])

# 선택 정렬 이용
for i in range(T):
    A = list(map(int, input().split()))
    for i in range(len(A)-1):
        minIdx = i
        for j in range(i, len(A)):
            if A[minIdx] > A[j]:
                minIdx = j

        A[minIdx], A[i] = A[i], A[minIdx]

    print(A[-3])

