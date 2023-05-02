# 배낭 무게 W
# i: 배낭에 넣을 물건을 나타내는 값(1...n)
# n : 물건의 개수
# 리턴 : K[n][W]

def knapsack():
    # 좌표에 0을 포함한 곳에는 0으로 채워준다(상품이 0개일 수 없고 무게가 0일 수 없으므로)
    for i in range(n+1):
        K[i][0] = 0
    for w in range(W+1):
        K[0][w] = 0


    for i in range(1, n+1):
        for w in range(1, W+1):
            if weight[i] > w:   # i번째 상품 크기가 현재 가방 크기보다 크면 넣을 수 없음
                K[i][w] = K[i-1][w]     # 값은 표 위 칸과 같다
            else:   # 가방 크기가 상품 크기보다 커서 넣을 수 있는 경우
                # 현재 무게 + 남은 무게 중 이 전에 구했던 무게의 값과 지금까지 구했던 현재 무게의 값 중 최대값을 구해야 함
                K[i][w] = max(K[i-1][w-weight[i]]+value[i], K[i-1][w])
    return K[n][W]


T = int(input())

for tc in range(1, T+1):
    W, n = map(int, input().split())
    weight = [0]    # 크기 넣을 리스트(숫자 1부터니까 0 넣어줌)
    value = [0]     # 가격 넣을 리스트

    K = [[0] * (W+1) for _ in range(n+1)]
    for _ in range(n):
        S, P = map(int, input().split())
        weight.append(S)
        value.append(P)
    print(f'#{tc} {knapsack()}')