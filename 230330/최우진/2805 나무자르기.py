N, M = list(map(int, input().split()))
tree = list(map(int, input().split()))

# 범위 지정
maxtree = max(tree)-1 # 최대 길이 나무 -1
mintree = maxtree - M # 최대길이 나무 - 필요한 나무 길이

# 이진 탐색 시작
s, e = mintree, maxtree # 시작점 끝점 지정

while s <= e: # 시작점이 끝점이 될때까지
    middle = (s+e)//2 # 중간 값
    t_len = 0 # 잘라진 나무 길이 구하기 위한 변수
    for t in tree: # 나무를 하나씩 돌면서
        if t > middle:  # 나무의 길이가 정해준 중간값보다 크면
            t_len += t-middle # 잘라 준다

    if t_len >= M: #자른 나무의 총 길이가 원하는 나무의 길이보다 크면
        s = middle + 1 # 시작점을 정해준 중간 값으로 바꿔주고
    else:  # 작으면
        e = middle - 1 # 끝점을 바꿔줌
    # print(s,e)

print(e)