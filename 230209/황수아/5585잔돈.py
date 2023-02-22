#SOL1 
# price = int(input())
# jan = 1000 - price
# money = [500, 100, 50,10,5]
# jan_lst = []
# while jan != 0:
#     if jan//500 != 0:
#         a = jan//500
#         jan_lst.append(a)
#         jan = jan - ((jan//500)*500)
#     if jan//100 != 0:
#         b = jan//100
#         jan_lst.append(b)
#         jan = jan - ((jan//100)*100)
#     if jan//50 != 0:
#         c = jan//50
#         jan_lst.append(c)
#         jan = jan - ((jan//50)*50)
#     if jan//10 != 0:
#         f = jan//10
#         jan_lst.append(f)
#         jan = jan - ((jan//10)*10)
#     if jan//5 != 0:
#         d = jan//5
#         jan_lst.append(d)
#         jan = jan - ((jan//5)*5)
#     else :
#         e = jan
#         jan_lst.append(e)
#         jan = jan - e
# sum = 0
# for k in jan_lst:
#     sum += k
# print(sum)


#SOL2
N = int(input())
money = [500,100,50,10,5,1] 
answer = 0
N = 1000-N

for m in  money :
    temp = (N//m)*m
    answer += N//m
    N -= temp
    if N == 0  : break

print(answer)