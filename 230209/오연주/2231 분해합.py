# 숫자 입력받음
Input = int(input())

# 분해합 인덱스에 생성자를 넣을 리스트를 만듦, 초기값은 전부 [0]으로 세팅
# 최대값이 100만이고 자릿수의 합은 100을 넘지 않을 것이기 때문에 넉넉하게 100개 추가
num_lst = [[0]]*1000100
# 최대값 백만
for i in range(1, 1000000):
    # 숫자 나눠서 i들의 분해합을 구해줌
    sep_lst = list(map(int, str(i)))
    numsum = i
    for j in sep_lst:
        numsum += j

    # 분해합에 맞는 생성자를 구하는 것이기 때문에 분해합의 인덱스 번호에 생성자를 넣어줌
    # 생성자가 여러개일 경우가 있다고 했으니 리스트에 추가하는 형식으로 넣어준다
    if num_lst[numsum] != [0]:
        num_lst[numsum].append(i)
    else:
        num_lst[numsum] = [i]

# num_lst의 인덱스(분해합)을 찾아가면 생성자들이 있음..
# 0이면 없는것 > 0 출력, 0이 아니면 가장 작은 수인 0번 인덱스 자리 출력
if num_lst[Input] == [0]:
    print(0)
else:
    print(num_lst[Input][0])