import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = [0]+A
s = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        s[i] = max(s[i], s[i-j]+A[j])
print(s[i])