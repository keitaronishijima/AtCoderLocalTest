import sys
input = sys.stdin.readline

n,x = map(int, input().split())
x -= 1
a=list(map(int, input().split()))
dummy = []
for i in range(n):
    dummy.append(0)
count = 0
while True:
    if dummy[x] == 0:
        dummy[x] = 1
        count += 1
        x = a[x] - 1
    else:
        break
print(count)
