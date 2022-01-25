import sys
from collections import defaultdict
input = sys.stdin.readline
s, t, x = map(int, input().split())
if s < t:
  if x>= s and x < t:
    print("Yes")
  else:
    print("No")
else:
  if x >= t and x < s:
    print("No")
  else:
    print("Yes")