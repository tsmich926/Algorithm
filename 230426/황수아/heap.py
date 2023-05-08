import heapq

# heappush

heap = []
heapq.heappush(heap, 50)
print(heap)
# 결과:[50]

heapq.heappush(heap, 10)
print(heap)
# 결과:[10,50]

heapq.heappush(heap, 5)
print(heap)
# 결과:[5,50,10]


# heapify
# 생성해둔 리스트가 있으면 heapify를 이용해 힙자료형으로 변환

heap2 = [50, 10, 20]
heapq.heapify(heap2)

print(heap2)
# 결과: [10,50,20]


# heappop
# 가장 작은 원소를 힙에서 제거
result = heapq.heappop(heap2)
print(result)
# 결과: 10
print(heap2)
# 결과: [20,50]



내림차순
정렬

from heapq import heappush, heappop

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
    print(heappop(heap)[1])  # index 1

결과
8
7
5
4
3
1

# 힙큐를
# 이용한
# 정렬

import heapq


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


# h = [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


