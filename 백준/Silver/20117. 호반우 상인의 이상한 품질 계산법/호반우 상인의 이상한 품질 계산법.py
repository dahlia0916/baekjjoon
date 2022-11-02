import sys
n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
s=0
s2=0
l.sort()
if n%2 ==0:
    for i in range(len(l)//2):
        s=s+l[n-i-1]*2
    s2=l[n//2]*n
else:
    for i in range((len(l)//2)):
        s=s+l[n-i-1]*2
    s=s+l[len(l)//2]
    s2=l[((n+1)//2)-1]*n

print(s)