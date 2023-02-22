# score= {'python': 80, 'django': 89, 'web': 83}
# score['python'] = 85
# total = sum(score.values())
# print(total/3)
# a = 3
# b = 6
# c = -5
# r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
# r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
# print(print(f'답은 : {r1:.4f}, {r2:.4f}'))

# 입력 예시
# a = '<p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>'
# print(a[3:-4])

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

#2-2
# str_lst = input("문자열을 입력하세요 : ")
# while 1:
#     print(f"{str_lst}", end="")
#     next = input()

#     if str_lst[-1] == next[0]:
#         print("pass")
#     else:
#         print("fail")
#         break 

# for i in str_lst(str(input)):
#     if ((str_lst[i] in str_lst[:i]) or (str_lst[i][-1] != str_lst[i+1][0])):
#         print('fail')         
#     else:
#         print('pass')

# stk = int(50000)
# vat = int(50000*0.15)
# sum_1 = stk+vat
# product = f'스테이크 {stk}\n+VAT {vat}\n총계￦ {sum_1}'
# print(product)

# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'


def wordR():
    wordL = []
    playing = True
    idx = 1

    while playing:
        word = input('단어를 입력해')
        if word == 'done':
            print('게임종료')
            playing = False
        if not len(wordL):
            wordL.append(word)
            continue
        
        wordL.append(word)        
        if wordL[idx -1][-1] != wordL[idx][0] or wordL[idx] in wordL[:idx]:
            print(f'{idx+1}번째 참가자 탈락!')
            playing = False
        else:
            idx += 1
wordR()
