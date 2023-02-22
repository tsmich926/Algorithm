T = int(input())
for tc in range(1,T+1):
    s = list(map(int,input().split()))
    for i in range(9):
        for k in range(i+1,10):
            if s[i] > s[k]: #오름차순으로 정렬
                s[i] ,s[k] = s[k],s[i]

    ans = s[-3] # 뒤에서 세번째수를 출력
    print(f'{ans}')