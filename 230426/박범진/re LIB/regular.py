import re

p = re.compile('[a-z]+')    # 띄어쓰기나 다른 문자가 나오면 종료, 보통 단어를 검사할때 쓴다
m = p.match("python")
print(m)

# m = p.match("python3333333")
# print(m)

# m = p.match("3 python")
# print(m)

# 이러면 이제 m은 match객체가 되었다

# match객체의 메서드에는 group, start, end, span이 있다


print(m.group())
print(m.start())
print(m.end())
print(m.span())


