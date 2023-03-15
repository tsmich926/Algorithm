#열별로 점수를 취합
#점수가 같으면 3점,2점을 많이 받은 사람으로 결정
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
score_lst = []
#후보들의 3점을 세는 배열
cnt_3 = []
#후보들의 2점을 세는 배열
cnt_2 = []
#열순회하며 후보들의 점수 모으기
for i in range(3):
    sum = 0
    cnt3 = 0
    cnt2 = 0         #열이 바뀔때마다 점수는 0으로 초기화
    for s in range(N): #column을 바꿔주는 반복문
        sum += arr[s][i]
        if arr[s][i] == 3:
            cnt3 += 1
        if arr[s][i] == 2:
            cnt2 += 1
    cnt_3.append(cnt3)
    cnt_2.append(cnt2)
    score_lst.append(sum) #score_lst에는 순서대로 후보1,2,3의 득점이 담김

score_max = 0
for score in range(len(score_lst)):
    if score_max < score_lst[score]:
        score_max = score_lst[score]
        
        if score_lst.count(score_max) == 1:
            print(score, score_max )
        # 최다득점이 동점으로 나타난 경우
        else :
            smax = 0
            for k in range(len(cnt_3)):
                if smax < cnt_3[k]:
                    smax = cnt_3[k]
                    print(k, score_lst[k])        #K번째 후보의 후승, K번째 후보의 득점 출력
