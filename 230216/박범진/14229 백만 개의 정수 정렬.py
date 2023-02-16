def quick_sort(arr):
    def sort(low, high):
        if high <= low:    # 왼쪽과 오른쪽이 같을때 (더이상 정렬할게 없을때) 종료
            return

        mid = partition(low, high)
        sort(low, mid - 1)    # 왼쪽부터 가운데-1까지 다시 정렬 시작
        sort(mid, high)       # 가운데부터 오른쪽까지 다시 정렬 시작

    def partition(low, high):
        pivot = arr[(low + high) // 2]    # 수가 중간값이 아니라 무작위로 중간에있는 숫자
        while low <= high:
            while arr[low] < pivot:    # 시작 인덱스(low)가 가리키는 값과 pivot 값을 비교해서 더 작은 경우 반복해서 시작 인덱스 값을 증가시킵니다. (pivot 값보다 큰데 좌측에 있는 값을 찾기 위해)
                low += 1
            while arr[high] > pivot:    # 끝 인덱스(high)가 가리키는 값과 pivot 값을 비교해서 더 작은 경우 반복해서 끝 인덱스 값을 감소시킵니다. (pivot 값보다 작은데 우측에 있는 값을 찾기 위해)
                high -= 1
            if low <= high:    # 두 인덱스가 아직 서로 교차해서 지나치치 않았다면 시작 인덱스(low)가 가리키는 값과 끝 인덱스(high)가 가리키는 값을 상호 교대(swap) 시킵니다. (잘못된 위치에 있는 두 값의 위치를 바꾸기 위해)
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1    # 상호 교대 후, 다음 값을 가리키기 위해 두 인덱스를 각자 진행 방향으로 한 칸씩 이동 시킵니다.
        return low
    t = sort(0, len(arr) - 1)
    return t

arr = list(map(int, input().split()))
quick_sort(arr)
print(arr[500000])




# 선택 정렬을 사용해서 제한시간 초과

# ARR = list(map(int, input().split()))
# N = 1000000
# for i in range(N-1):
#     min_idx = i
#     for j in range(i+1, N):
#         if ARR[j] < ARR[min_idx]:
#             min_idx = j
#     ARR[j], ARR[min_idx] = ARR[min_idx], ARR[j]
# print(ARR[500000])



# 버블 정렬을 사용해서 제한시간 초과
# ARR = list(map(int, input().split()))
# N = 1000000
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if ARR[j] > ARR[j+1]:
#             ARR[j], ARR[j+1] = ARR[j+1], ARR[j]
#
# print(ARR[500000])