import sys
input = sys.stdin.readline

a, N = map(int, input().split())

def dfs(a,x):
    if a == x:
        return 0
    if 