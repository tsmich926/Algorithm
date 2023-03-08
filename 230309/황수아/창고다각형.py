N =int(input())
lst= [0]*1001
mx_i =mx = 0

for _ in range(N):
    L,H=map(int,input().split())
    lst[L] = H  #L위치에 H를 기록
    if mx < H :
        mx_i,mx = L,H

#왼쪽검사
ans=mx =0
for i in range(mx_i+1):
    mx =max(mx,lst[i])
    ans += mx

#오른쪽 검사
mx = 0
for i in range(1000,mx_i,-1):
    mx =max(mx,lst[i])
    ans += mx
print(ans)