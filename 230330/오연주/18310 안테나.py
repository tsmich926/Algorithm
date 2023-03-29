import sys
input = sys.stdin.readline
T = int(input())
lst = list(map(int, input().split()))

lst.sort()

print(lst[(T-1)//2])