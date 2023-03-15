def check(lst, num):
    global flst
    if lst:
        root = len(lst)//2
        flst[num].append(lst[root])
        check(lst[:root], num+1)
        check(lst[root+1:], num+1)
    return flst



N = int(input())
lst = list(map(int, input().split()))
flst = [[] for _ in range(N)]
check(lst, 0)

for i in flst:
    print(*i)
