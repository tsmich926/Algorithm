change = [500, 100, 50, 10, 5, 1]
N = int(input())
money = 1000 - N # 남은돈
count = 0
#남은돈이 0원이 될 때까지 change의 앞에서부터 빼고 change보다 money가 작아지면 다음으로 넘어감
while money != 0: 
    for i in range(6):
        while money >= change[i]:
            money -= change[i]
            count += 1
print(count)