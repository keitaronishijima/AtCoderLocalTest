import sys
import math
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(str, input().split()))
t = list(map(str, input().split()))

pos = 0

for i in range(n):
  if t[pos] == s[i]:
    print("Yes")
    pos = pos + 1
  else:
    print("No")