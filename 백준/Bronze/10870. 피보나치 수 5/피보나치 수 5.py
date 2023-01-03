import sys

n=int(sys.stdin.readline())
s = [0 for _ in range(n)]
if n<=1:
    print(n)
else:
    s[1]=1
    for i in range(2,n):
        s[i]=s[i-1]+s[i-2]
    print(s[n-1]+s[n-2])