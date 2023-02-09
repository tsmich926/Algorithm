dwarf1 = int(input())
dwarf2 = int(input())
dwarf3 = int(input())
dwarf4 = int(input())
dwarf5 = int(input())
dwarf6 = int(input())
dwarf7 = int(input())
dwarf8 = int(input())
dwarf9 = int(input())

d_lst = [dwarf1, dwarf2, dwarf3, dwarf4, dwarf5, dwarf6, dwarf7, dwarf8, dwarf9]
d_lst.sort()

min = 0 # 7개 더했을 때 최솟값
i = 0
while i < 7:
    min += d_lst[i]
    i += 1
num = 100 - min
for i in range(9):
    for j in range(7, 9):
        if d_lst[j] - d_lst[i] == num:
            d_lst.pop(i)
            break
res = d_lst[:7]
print(res)