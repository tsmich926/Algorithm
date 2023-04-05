from itertools import combinations, permutations
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

nums = []
for i in range(n):
    nums.append(i)

lis = list(combinations(nums,n//2))

lis2= []
for start in lis:
    stat1 = 0
    stat2 = 0
    start_list = []

    nums = []
    for i in range(n):
        nums.append(i)

    for i in start:
        nums.remove(i)

    num = nums
    num_list = []

    start_list = list(combinations(start,2))
    num_list = list(combinations(num, 2))
    # print(start_list)
    # print(num_list)

    for i in start_list:
        stat1 += arr[i[0]][i[1]] + arr[i[1]][i[0]]

    for j in num_list:
        stat2 += arr[j[0]][j[1]] + arr[j[1]][j[0]]

    lis2.append(abs(stat1-stat2))
print(min(lis2))