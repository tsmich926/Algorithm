import sys
input = sys.stdin.readline

K = int(input())
input2 = list(map(int, input().split()))
tree = [[] for _ in range(K)]


#배열의 중간값이 루트
def makeTree(arr, x):
    mid = (len(arr) // 2)
    tree[x].append(arr[mid])
    if len(arr) == 1:
        return
    makeTree(arr[:mid], x + 1)
    makeTree(arr[mid + 1:], x + 1)


makeTree(input2, 0)
for i in range(K):
    print(*tree[i])