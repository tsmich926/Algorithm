num = int(input())
lis = []
for i in range(1, num):
    nums = list(map(int, str(i)))
    numss = ''.join(map(str, nums))
    nums.append(int(numss))
    sumV = 0
    for i in nums:
        sumV += i
    if sumV == num:
        lis.append(i)

if len(lis) == 0:
    print('0')
else:
    print(min(lis))