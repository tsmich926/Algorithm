import sys
sys.stdin = open('input.txt', 'r')

def preOrder(root):                    # 전위, 중위, 후위 순회 함수 생성
    if root:
        print(chr(root+64), end= '')
        preOrder(leftC[root])
        preOrder(rightC[root])
def inOrder(root):
    if root:
        inOrder(leftC[root])
        print(chr(root+64), end='')
        inOrder(rightC[root])

def postOrder(root):
    if root:
        postOrder(leftC[root])
        postOrder(rightC[root])
        print(chr(root+64), end= '')


N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
leftC = [0]*(N+1)
rightC = [0]*(N+1)
for i in range(N):
    for j in range(3):
        if arr[i][j].isupper():
            arr[i][j] = ord(arr[i][j]) - 64          # 알파벳 순으로 숫자로 변환(A : 1, B: 2 ...)
        if arr[i][j] =='.':                          # '.' 은 0으로 변환
            arr[i][j] = 0

for i in range(N):
    leftC[arr[i][0]] = arr[i][1]             # 왼쪽 오른쪽 자식 따로 인접배열 생성
    rightC[arr[i][0]] = arr[i][2]

preOrder(1)
print()
inOrder(1)
print()
postOrder(1)
print()