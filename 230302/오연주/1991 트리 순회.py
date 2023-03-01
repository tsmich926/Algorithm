def preorder(root):
    if root:
        print(chr(root+64), end='')
        preorder(c1[root])
        preorder(c2[root])

def inorder(root):
    if root:
        inorder(c1[root])
        print(chr(root+64), end='')
        inorder(c2[root])

def postorder(root):
    if root:
        postorder(c1[root])
        postorder(c2[root])
        print(chr(root+64), end='')


N = int(input())
c1 = [0] * (N+1)
c2 = [0] * (N+1)

for _ in range(N):
    n, l, r = map(str, input().split())
    if l != '.':
        c1[ord(n) - 64] = ord(l)-64
    if r != '.':
        c2[ord(n) - 64] = ord(r)-64

preorder(1)
print()
inorder(1)
print()
postorder(1)