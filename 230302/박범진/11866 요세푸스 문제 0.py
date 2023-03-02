N, K = map(int, input().split())
lst = [i for i in range(1, N+1)]
ans = []
while lst:    
    i = 0    # 몇번째 숫자를 뺄지를 정하는 i와 K
    while i < K-1:    # 배열의 순서를 바꾸기 위해 이 while이 도는동안 앞에있는 수를 뒤로 빼기
        v = lst.pop(0)
        i += 1
        lst.append(v)
    t = lst.pop(0)    # while이 다돌았으면 그때 노렸던 숫자를 정답리스트에 추가!
    ans.append(t)
list_ans = str(ans)[1:-1]
print(f'<{list_ans}>')