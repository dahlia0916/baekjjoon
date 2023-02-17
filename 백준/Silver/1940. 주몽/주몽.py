import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
if m>100000:
    print(0)
else:
    l=list(map(int,sys.stdin.readline().split()))
    s=0
    for i in range(n):
        for j in range(i+1,n):
            if l[i]+l[j]==m:
                s=s+1
    print(s)