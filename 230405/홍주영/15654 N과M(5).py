import sys
sys.stdin = open('input.txt', 'r')
from itertools import permutations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in permutations(lst, M):
    print(*i)