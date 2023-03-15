
N,K =map(int,input().split())
lst = []
ans =[]
sp = 0
for i in range(1,N+1):
    lst.append(i)

while len(lst):
    sp = (sp+(K-1)) % len(lst) #K만큼 이동을 했을때 인덱스를 넘어버릴 수 있기때문
    ans.append(lst.pop(sp)) 

#출력포맷 변경해줄 것
#ans 출력시 [3, 6, 2, 7, 5, 1, 4]로 나옴
# ans.replace('[', '<')
# print(ans)

print("<", ', '.join(str(i) for i in ans), ">", sep = '')