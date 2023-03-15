T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    name = [input() for _ in range(N)]


    # 버블정렬 사용 : 제한시간 초과
   # for i in range(N-1, -1, -1):
    #     for j in range(i):
    #         if len(name[j]) > len(name[j+1]):
    #             name[j], name[j+1] = name[j+1], name[j]
    #         elif len(name[j]) == len(name[j+1]):
    #             if name[j] > name[j+1]:
    #                 name[j], name[j + 1] = name[j + 1], name[j]

    # sort 한번 사용 : 제한시간 초과
    # namelst = []
    # for i in name:
    #     namelst.append((len(i), i))
    #
    # nname = sorted(namelst)

    # name2 = []
    # for i in nname:
    #     if i[1] in name2:
    #         pass
    #     else:
    #         name2.append(i[1])
    #
    # print(f'#{tc}', *name2, sep='\n')

    name2 = list(set(name))  # 예시 2번을 보면 같은 단어는 나오지 않음. 세트로 없애줌
    name2 = sorted(name)
    print(f'#{tc}', *name2, sep='\n')