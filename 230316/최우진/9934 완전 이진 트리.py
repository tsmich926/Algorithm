k = int(input())
arr = list(map(int, input().split()))

lis = [[] for _ in range(k)]


def dfs(arr, dep):
    # arr에서 루트의 인덱스
    mid = (len(arr) // 2)

    # 깊이의 노드들을 모두 추가시킴
    lis[dep].append(arr[mid])

    # 계속 나눠줬을 때 arr의 길이가 1이 되면 stop
    if len(arr) == 1:
        return

    dfs(arr[:mid], dep + 1)
    dfs(arr[mid + 1:], dep + 1)


dfs(arr, 0)

for i in lis:
    print(*i)