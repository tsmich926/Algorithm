sen = input()
word = list(input())
lst = []

for s in sen:
    lst.append(s)    # if문으로 조건에 맞는지 비교하기 전에 우선 문자를 lst에 더함
    if lst and lst[-1:-(len(word)+1):-1] == word[::-1]:    # 그리고 lst의 맨 뒤부터 비교하고자하는 word의 길이까지비교한 후, word를 뒤집은 문자와 일치한다면
        for i in range(len(word)):    # word의 길이만큼 pop
            lst.pop()

if lst:
    print(''.join(lst))
else:
    print('FRULA')