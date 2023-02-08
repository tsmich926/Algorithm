#백준 백설공주와 일곱난쟁이

lst = []
for i in range(9):
    n = int(input())
    lst.append(n)

sum = 0
for m in lst:
    sum += m
e = sum - 100 


for n in range(len(lst)):
    for k in range(n+1,9): 
            if lst[n] + lst[k] == e :
                a = lst[n]
                b = lst[k]
lst.remove(a)
lst.remove(b)
for t in lst:
    print(t)