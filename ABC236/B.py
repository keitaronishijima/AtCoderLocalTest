import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for i in range(1, n+1):
    ans = ans + i
ans = ans * 4
size = 4 * n
s = list(map(int, input().split()))
l = len(s)
sum = 0
for i in range(l):
    sum = sum + s[i]
print(ans-sum)