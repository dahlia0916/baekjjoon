import sys
N,M = map(int,sys.stdin.readline().split())
color=[]
for i in range(M):
    color.append(int(sys.stdin.readline()))
left=1
right=max(color)
while left<=right:
    mid=(right+left)//2
    n=0
    for j in range(len(color)):
        if color[j]%mid !=0:
            n=n+color[j]//mid+1
        else:
            n=n+color[j]//mid
    if n>N:
        left=mid+1
    else:
        right=mid-1

print(left)