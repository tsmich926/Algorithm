n = int(input())
houses = list(map(int, input().split()))

# 집들을 위치순으로 정렬
houses.sort()

# 중간값을 선택
med = houses[(n-1)//2]

# 중간값이 안테나의 위치
print(med)