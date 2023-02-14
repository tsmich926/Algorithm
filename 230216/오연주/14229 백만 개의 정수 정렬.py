import sys
sys.stdin=open('input.txt', 'rt')


# 수업시간... 배운 정렬들 전부 시간초과
# 퀵정렬 활용
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot, tail = array[0], array[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]

    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)


lst = list(map(int, input().split()))
lst = quick_sort(lst)
print(lst[500000])