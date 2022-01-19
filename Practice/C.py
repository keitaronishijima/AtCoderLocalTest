import sys
from collections import defaultdict
input = sys.stdin.readline
 
N, Q =  map(int, input().split())
A = list(map(int, input().split()))
a = sorted(A)
 
m = defaultdict(list)
for i in range(N):
  m[A[i]].append(i+1)
 
for _ in range(Q):
  x, y = map(int, input().split())
  if len(m[x]) >= y:
    print(m[x][y-1])
  else:
    print(-1)