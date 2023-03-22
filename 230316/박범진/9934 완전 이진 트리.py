K = int(input())
arr = list(map(int, input().split()))
ans = [[] for _ in range(K)]
def Tree(arr, height):
    mid = (len(arr)//2)
    ans[height].append(arr[mid])
    if len(arr) == 1:
        return

    Tree(arr[:mid], height+1)
    Tree(arr[mid+1:], height+1)

Tree(arr, 0)

for i in ans:
    print(*i)



