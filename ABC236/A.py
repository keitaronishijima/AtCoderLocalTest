import sys
from collections import defaultdict
input = sys.stdin.readline
s = list(input())
a,b = map(int, input().split())
a = a - 1
b = b - 1
tmp = s[a]
s[a] = s[b]
s[b] = tmp
ans = ""
for i in range(len(s)):
    ans = ans + s[i]
print(ans)