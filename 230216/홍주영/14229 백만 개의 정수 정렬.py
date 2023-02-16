import sys
sys.stdin = open('input.txt', 'r')

def quick_sort(A):                                  # 퀵솔트 정렬을 이용하여 풀이
    if len(A) <= 1:
        return A
    pivot, tail = A[0], A[1:]

    leftside = [x for x in tail if x <= pivot]
    righside = [x for x in tail if x > pivot]

    return quick_sort(leftside) + [pivot] + quick_sort(righside)       # 재귀를 사용해서 시간이 오래걸림



A = list(map(int, input().split()))
sort_A = quick_sort(A)
print(sort_A[500000])