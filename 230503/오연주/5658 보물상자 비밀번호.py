T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(str, input()))

    nums = []
    for i in range(N//4):
        for j in range(4):
            word = "".join(num[(N//4)*j:(N//4)*(j+1)])
            wordint = int(word, 16)
            if wordint not in nums:
                nums.append(wordint)
        popNum = num.pop(-1)
        num.insert(0, popNum)


    flst = sorted(nums, reverse=True)
    print(f'#{tc} {flst[K-1]}')