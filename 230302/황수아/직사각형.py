for tc in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2= map(int,input().split())

    # 공통부분 없음
    if (x2 > p1) or (p2 > x1) or (q1 < y2) or (y1 > q2):
        ans = "d"

    # 점 1개에서 만날 때
    if (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2) or (x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1):
        ans= "c"

    # 변이 만날 때
    if p1 == x2 :
        if (q1<q2 and y2<q1<q2) or (q1>q2 and q1<q2<y1):
            ans = "b"
    if x1 == p2 :
        if (x1<p2 and y1<y2<q1) or (x1>p2 and q2<y1<y2):
            ans = "b"
    if y1 == q2 :
        if (p1>p2 and x1<p2<p1 ) or (p1<p2 and x2<p1<p2):
            ans = "b"
    
    if y2 == q1:
        if () or ():
            ans = "b"

    #나머지 직사각형(겹칠때)
    ans =  "a"
    print(ans)

