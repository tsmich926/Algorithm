import sys
from functools import reduce
# 검색하다 보니 reduce 함수를 사용하면 뚝딱이다.
# 람다 응용까지 해봄
# reduce는 데이터를 누적해준다 n!를 만들어줌

N = int(sys.stdin.readline())
f = reduce(lambda x, y: x * y, [i for i in range(1, N+1)])
answer = 0
for i in reversed(str(f)):
    if i == '0':
        answer += 1
print(answer)