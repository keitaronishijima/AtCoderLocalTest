import sys
import math
from collections import defaultdict
input = sys.stdin.readline

m,n = input().split()
m = m[::-1]
n = n[::-1]
l = min(len(m), len(n) )
ok = False
for i in range(l):
  if int(m[i]) + int(n[i]) >= 10 and ok is False:
    ok = True
    print("Hard")
if not ok:
  print("Easy")