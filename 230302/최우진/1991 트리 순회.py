N = int(input())
tree = {}


# 트리를 구현하는 방법 : dictionary 사용
# root를 키로/ left, right를 value로 할당
for _ in range(N):
    root, left, right = list(input().split())
    tree[root] = [left, right] #

# 전위 실행 순서 - > 부모, 좌, 우
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


# 중위 실행 순서 - > 좌, 부모, 우
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right

# 후위 실행 순서 - > 좌, 우, 부모
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root


preorder('A')
print()
inorder('A')
print()
postorder('A')