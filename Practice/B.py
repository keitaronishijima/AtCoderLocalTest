import sys
input = sys.stdin.readline

s1 = input()
s2 = input()
ans = ''
l = len(s1)
for i in range(26):
    test = s1
    for j in range(l):
        ans+=(ord(s1[j]) + i)
        if s1[j] > 'z':
            dif = ord(s1[i]) - ord('z') - 1
            ans+=(ord('a') + dif)
    if s1 == s2:
        print('Yes')
        exit()

print('No')

