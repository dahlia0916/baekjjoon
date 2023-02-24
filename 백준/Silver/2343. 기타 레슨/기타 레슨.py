import sys
N,M = map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))

total=sum(l)
left=0
right=10000000000
sol=total
while left<=right:
    mid=(left+right)//2
    if mid < max(l):
        left = mid+1
        continue
    cnt,temp=1,0
    for i in range(len(l)):
        if temp + l[i]<=mid:
            temp=temp+l[i]
        else:
            temp = l[i]
            cnt=cnt+1
    if cnt <= M:
        right=mid-1
        sol=min(sol,mid)
    else:
        left=mid+1
print(sol)