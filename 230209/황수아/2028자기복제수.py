T = int(input())
for tc in range(T):
    n = int(input())
    suqre = str(n * n)
    lenth = len(str(n))
    if suqre[-lenth:] == str(n) :
        print('Yes')
    else :
        print('No')