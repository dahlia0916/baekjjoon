import sys
r,c,K = map(int,sys.stdin.readline().split())
l=[]
for i in range(r):
    l.append(list(map(str,sys.stdin.readline().strip("\n"))))
v=[[0]*c for _ in range(r)]
cnt=0

def check(y,x,k):
    global cnt
    if k==K:
        if (y,x)==(0,c-1):
            cnt=cnt+1
    else:
        v[y][x]=1
        for i in range(4):
            dy=[1,0,-1,0]
            dx=[0,1,0,-1]
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<r and 0<=nx<c and v[ny][nx]==0 and l[ny][nx] != "T":
                v[ny][nx]=1
                check(ny,nx,k+1)
                v[ny][nx]=0

v[r-1][0]=1
check(r-1,0,1)
print(cnt)