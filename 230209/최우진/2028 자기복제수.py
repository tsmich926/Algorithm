TC = int(input())
for tc in range(TC):
    num = int(input())
    num_s = str(num)

    nums = num**2
    nums_s = str(nums)

    if int(nums_s[-len(num_s):]) == num:
        print('YES')
    else:
        print('NO')