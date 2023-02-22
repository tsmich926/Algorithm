s = input()
num_dic = {'ABC':2 ,'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8 ,'WXYZ':9, 'operation':0}
ss= num_dic.keys()
alpa_lst = []
for i in ss:
    alpa_lst.append(i)
# print(alpa_lst)
num_lst = [] 
for m in s:
    for k in range(len(alpa_lst)):
        if m in alpa_lst[k]:
            number = num_dic[alpa_lst[k]]
    num_lst.append(number)
# print(num_lst)
sigan = sum(num_lst) + (1*len(num_lst))
print(sigan)

# s = input()
# num_dic = {'ABC':2 ,'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8 ,'WXYZ':9, 'operation':0}
# ss= num_dic.keys()
# alpa_lst = []
# for i in s:
#         for k in ss:
#         if i in k:
#             number = num_dic[k]
#             print(number)

# for m in s:
#     for k in range(len(alpa_lst)):
#         if m in alpa_lst[k]:
#             number = num_dic[alpa_lst[k]