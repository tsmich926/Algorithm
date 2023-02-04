# 문자열 입력
Input = input()

# 문자열 하나하나 나눠서 아스키코드 숫자로 리스트에 저장
word_list = []
for i in Input:
    word_list.append(ord(i))

# 합 초기값 세팅
a = 0

# 아스키코드 숫자 나눠서 합 초기값에 각각 더해줌
for i in word_list:
    if 87 <= i:
        a += 10
    elif 84<= i:
        a += 9
    elif 80 <= i:
        a += 8
    elif 77 <= i:
        a += 7
    elif 74 <= i:
        a += 6
    elif 71 <= i:
        a += 5
    elif 68 <= i:
        a += 4
    elif 65 <= i:
        a += 3

# 합 출력
print(a)