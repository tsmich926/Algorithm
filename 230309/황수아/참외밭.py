K = int(input())
direction = [] #방향을 담는 리스트
distance = [] #거리를 담는 리스트

for _ in range(6): #여섯개 변의 길이와 방향을 입력받음
    a, b = map(int,input().split())
    direction.append(a)
    distance.append(b)

pattern = [(2, 4), (3, 2), (1, 3), (4, 1)] #움푹파인 부분의 방향
idx = -1 #인덱스 초기화

for i in range(6): #여섯개의 방향을 검사
    if (direction[i], direction[(i + 1) % 6]) in pattern: #움푹파인 부분의 인덱스를 알아내기 위함
        idx = i
        break

big = distance[(idx + 3) % 6] * distance[(idx + 4) % 6] #큰 사각형의 넓이
small = distance[idx] * distance[(idx + 1) % 6] #작은 사각형의 넓이

print((big - small) * K) #큰사각형*작은사각형*참외