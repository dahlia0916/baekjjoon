import sys
n,k=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
psum=[0]*(n+1)
ret=-100000004
for i in range(1,n+1):
    psum[i]=psum[i-1]+l[i-1]
for i in range(k,n+1):
    ret=max(ret,psum[i]-psum[i-k])
print(ret)