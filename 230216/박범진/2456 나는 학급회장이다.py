def my_sum(lst):    # 총합을 구하는 함수
    sumV = 0
    for i in lst:
        sumV += i
    return sumV

def my_max(lst):    # 최대값을 구하는 함수
    maxV = 0
    for i in lst:
        if i > maxV:
            maxV = i
    return maxV

def count_3(lst):    # 3의 개수를 세는 함수
    count = 0
    for i in lst:
        if i == 3:
            count += 1
    return count

def count_2(lst):    # 2의 개수를 세는 함수
    count = 0
    for i in lst:
        if i == 2:
            count += 1
    return count

N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]
s1 = []
s2 = []
s3 = []
for i in range(N):
    s1.append(ARR[i][0])
    s2.append(ARR[i][1])
    s3.append(ARR[i][2])

def president(s1, s2, s3):
    if my_sum(s1) > my_sum(s2) and my_sum(s1) > my_sum(s3):    # 확실히 나머지 둘보다 클때
        return 1, my_sum(s1)
    elif my_sum(s1) == my_sum(s2):    # 둘 중 하나와 같을 시 3의 개수를 비교
        if count_3(s1) > count_3(s2):
            return 1, my_sum(s1)
    elif my_sum(s1) == my_sum(s3):
        if count_3(s1) > count_3(s3):
            return 1, my_sum(s1)
    elif my_sum(s1) == my_sum(s2):    # 3의 개수도 같을시 2의 개수를 비교
        if count_2(s1) > count_2(s2):
            return 1, my_sum(s1)
    elif my_sum(s1) == my_sum(s3):
        if count_2(s1) > count_2(s3):
            return 1, my_sum(s1)
    if my_sum(s2) > my_sum(s1) and my_sum(s2) > my_sum(s3):    # 확실히 나머지 둘보다 클때
        return 2, my_sum(s2)
    elif my_sum(s2) == my_sum(s1):    # 둘 중 하나와 같을 시 3의 개수를 비교
        if count_3(s2) > count_3(s1):
            return 2, my_sum(s2)
    elif my_sum(s2) == my_sum(s3):
        if count_3(s2) > count_3(s3):
            return 2, my_sum(s2)
    elif my_sum(s2) == my_sum(s1):     # 3의 개수도 같을시 2의 개수를 비교
        if count_2(s2) > count_2(s1):
            return 2, my_sum(s2)
    elif my_sum(s2) == my_sum(s3):
        if count_2(s2) > count_2(s3):
            return 2, my_sum(s2)
    if my_sum(s3) > my_sum(s1) and my_sum(s3) > my_sum(s2):    # 확실히 나머지 둘보다 클때
        return 3, my_sum(s3)
    elif my_sum(s3) == my_sum(s1):    # 둘 중 하나와 같을 시 3의 개수를 비교
        if count_3(s3) > count_3(s1):
            return 3, my_sum(s3)
    elif my_sum(s3) == my_sum(s2):
        if count_3(s3) > count_3(s2):
            return 3, my_sum(s3)
    elif my_sum(s3) == my_sum(s1):     # 3의 개수도 같을시 2의 개수를 비교
        if count_2(s3) > count_2(s1):
            return 3, my_sum(s3)
    elif my_sum(s3) == my_sum(s2):
        if count_2(s3) > count_2(s2):
            return 3, my_sum(s3)

    return 0, my_max([my_sum(s1), my_sum(s2), my_sum(s3)])    # 모두다 아닐시

print(*president(s1, s2, s3))