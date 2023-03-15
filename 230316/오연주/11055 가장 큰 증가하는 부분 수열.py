N = int(input())
lst = list(map(int, input().split()))
sumlst = [lst[0]]

for i in range(1, N):
    maxV = 0
    for j in range(i):
        if lst[i] > lst[j]:
            sumV = sumlst[j]+lst[i]
            if sumV > maxV:
                maxV = sumV
        else:
            sumV = lst[i]
            if sumV > maxV:
                maxV = sumV
    sumlst.append(maxV)

print(max(sumlst))